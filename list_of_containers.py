from azure.storage.blob import BlobServiceClient
from config import connection_string

# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# List all containers in the storage account
print("Listing containers in the storage account:")
containers = blob_service_client.list_containers()
for container in containers:
    print(f"- {container.name}")