from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from config import SEARCH_ENDPOINT, SEARCH_INDEX, SEARCH_API_KEY

search_client = SearchClient(
    endpoint=SEARCH_ENDPOINT,
    index_name=SEARCH_INDEX,
    credential=AzureKeyCredential(SEARCH_API_KEY)
)

def search_documents(query):

    results = search_client.search(search_text=query)

    output = []

    for r in results:
        output.append({
            "title": r.get("title"),
            "content": r.get("content")
        })

    return output