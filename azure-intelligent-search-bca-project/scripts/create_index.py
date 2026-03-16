from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SimpleField,
    SearchableField
)
from azure.core.credentials import AzureKeyCredential

endpoint = "https://your-search-service.search.windows.net"
key = "YOUR_ADMIN_KEY"
index_name = "documents-index"

client = SearchIndexClient(endpoint, AzureKeyCredential(key))

fields = [
    SimpleField(name="id", type="Edm.String", key=True),
    SearchableField(name="title", type="Edm.String"),
    SearchableField(name="content", type="Edm.String")
]

index = SearchIndex(name=index_name, fields=fields)

client.create_index(index)

print("Search index created successfully")