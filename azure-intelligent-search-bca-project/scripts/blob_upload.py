from azure.storage.blob import BlobServiceClient

connection_string = "YOUR_CONNECTION_STRING"
container_name = "documents"

blob_service = BlobServiceClient.from_connection_string(connection_string)

container_client = blob_service.get_container_client(container_name)

with open("sample.txt", "rb") as data:
    container_client.upload_blob(name="sample.txt", data=data)