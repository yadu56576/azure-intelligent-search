# index_documents.py
# Script to create a search index and upload internal documents

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SimpleField,
    SearchableField
)

# Azure Search Configuration
endpoint = "https://your-search-service.search.windows.net"
api_key = "YOUR_AZURE_SEARCH_API_KEY"
index_name = "internal-documents-index"

# Create credential
credential = AzureKeyCredential(api_key)

# Create Index Client
index_client = SearchIndexClient(endpoint=endpoint, credential=credential)

# Define Index Fields
fields = [
    SimpleField(name="id", type="Edm.String", key=True),
    SearchableField(name="title", type="Edm.String"),
    SearchableField(name="content", type="Edm.String")
]

# Create Index
index = SearchIndex(name=index_name, fields=fields)

try:
    index_client.create_index(index)
    print("Search index created successfully.")
except Exception:
    print("Index already exists.")

# Create Search Client
search_client = SearchClient(
    endpoint=endpoint,
    index_name=index_name,
    credential=credential
)

# Sample Internal Documents (based on project use case)
documents = [
    {
        "id": "1",
        "title": "HR Leave Policy",
        "content": "Employees are entitled to 20 days of annual leave per year."
    },
    {
        "id": "2",
        "title": "Finance Expense Guidelines",
        "content": "All expense claims must be approved by the finance department."
    },
    {
        "id": "3",
        "title": "IT Password Reset Procedure",
        "content": "Employees can reset their passwords through the IT portal."
    }
]

# Upload Documents
result = search_client.upload_documents(documents=documents)

print("Documents successfully indexed into Azure Cognitive Search.")