import requests
from bs4 import BeautifulSoup


def fetch_webpage(url: str):

    if url:

        response = requests.get(url=url)

        if response.status_code == 200:
            try:
                # decode using response encoding if available
                html = response.content.decode(response.encoding or "utf-8", errors="ignore")

                soup = BeautifulSoup(html, "html.parser")

                # remove unnecessary tags
                for tag in soup(["script", "style", "noscript", "header", "footer", "nav", "aside", "form"]):
                    tag.decompose()

                # get clean text
                text = soup.get_text(separator=" ")

                # normalize whitespace
                cleaned_text = " ".join(text.split())

                return {"url": url, "content": cleaned_text}

            except Exception as e:
                return {"url": url, "content": f"Parsing Error: {str(e)}"}

        else:
            return {"url": url, "content": "An Error Occured While Fetching Webpage"}

    else:
        return {"url": url, "content": "URL Not Provided."}