## script to create a storage account in azure

from azure.identity import DefaultAzureCredential, ClientSecretCredential
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import StorageAccountCreateParameters, Sku, SkuName, Kind
from config import subscription_id, resource_group_name, storage_account_name, location, \
                    tenant_id, client_id, client_secret

# Authenticate using ClientSecretCredential
credential = ClientSecretCredential(tenant_id, client_id, client_secret)
storage_client = StorageManagementClient(credential, subscription_id)


# Create the storage account
storage_async_operation = storage_client.storage_accounts.begin_create(
    resource_group_name,
    storage_account_name,
    StorageAccountCreateParameters(
        sku=Sku(name=SkuName.standard_ragrs),
        kind=Kind.storage_v2,
        location=location
    )
)
storage_account = storage_async_operation.result()

print(f'Storage account {storage_account.name} created successfully.')
