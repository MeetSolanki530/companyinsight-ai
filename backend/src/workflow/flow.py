from langgraph.constants import START, END
from langgraph.graph import StateGraph

from src.models.flow_model import WorkflowState

from src.agents.website_analysis import get_website_analysis_agent_response
from src.agents.company_analysis import get_company_analysis_agent_response

from src.tools.website_scraper import fetch_webpage

class Graph:

    def __init__(self):
        self.workflow = create_workflow()

    def run(self, url : str):
        initial_state = WorkflowState(
            url=url,
            website_content="",

        )

        result = self.workflow.invoke(initial_state)
        return result["analysis_result"]

### Node 1 Website Fetch Node

def fetch_website_content_node(state : WorkflowState):
    
    url = state.url

    ### Call LLM Decide to use the tool

    response = get_website_analysis_agent_response(url=url)

    website_content = ""

    ## check if tool_call exist or not

    if hasattr(response, 'tool_calls') and response.tool_calls:

        for tool_call in response.tool_calls:

            if tool_call["name"] == "fetch_webpage":
                tool_result = fetch_webpage(**tool_call["args"])
                website_content = tool_result.get("content", "")

    state.website_content = str(website_content)

    return state


### Node 2 : Company Analysis Node

def analyze_company_node(state: WorkflowState):

    content = state.website_content

    response = get_company_analysis_agent_response(content)

    state.analysis_result = response.model_dump()

    return state


### Creating Graph

def create_workflow():
    
    graph = StateGraph(WorkflowState)

    # nodes

    graph.add_node("fetch_website_content", fetch_website_content_node)
    graph.add_node("analyze_company",analyze_company_node)

    # define edges

    graph.add_edge(START, "fetch_website_content")
    graph.add_edge("fetch_website_content","analyze_company")
    graph.add_edge("analyze_company", END)

    # compile graphs

    workflow = graph.compile()

    return workflow


if __name__ == "__main__":

    print("\n--- Running Company Insight Workflow Test ---\n")

    # example test url
    test_url = "https://stripe.com"

    graph_runner = Graph()

    result = graph_runner.run(test_url)

    print("\n--- Final Analysis Result ---\n")
    print(result)