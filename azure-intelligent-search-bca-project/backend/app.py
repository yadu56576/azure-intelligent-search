from flask import Flask, request, jsonify
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import config

app = Flask(__name__)

# Azure Search Configuration
endpoint = config.SEARCH_ENDPOINT
index_name = config.SEARCH_INDEX
api_key = config.SEARCH_API_KEY

# Create Search Client
credential = AzureKeyCredential(api_key)

search_client = SearchClient(
    endpoint=endpoint,
    index_name=index_name,
    credential=credential
)

@app.route("/")
def home():
    return "Azure Intelligent Search API is running."

# Search API
@app.route("/search", methods=["GET"])
def search_documents():
    query = request.args.get("q")

    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400

    results = search_client.search(query)

    documents = []

    for result in results:
        documents.append({
            "title": result.get("title"),
            "content": result.get("content")
        })

    return jsonify(documents)

if __name__ == "__main__":
    app.run(debug=True)