## Create an App using Python.
## in the Azure Storage Account which is Created.

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from config import connection_string


# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Create a container
container_name = "ameercontainer123"
container_client = blob_service_client.create_container(container_name)
print(f"Container '{container_name}' created successfully.")

# Upload a blob
blob_name = "ameer123.txt"
blob_client = container_client.get_blob_client(blob_name)

with open("ameer123.txt", "w") as file:
    file.write("Hello, Azure Blob Storage!")

with open("ameer123.txt", "rb") as data:
    blob_client.upload_blob(data)
    print(f"Blob '{blob_name}' uploaded to container '{container_name}'.")

# List blobs in the container
print("Listing blobs in the container:")
blobs = container_client.list_blobs()
for blob in blobs:
    print(f"- {blob.name}")