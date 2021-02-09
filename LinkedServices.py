# Add the following code to the Main method that creates an Azure Storage linked service.

# We create linked services in a data factory to link your data stores and compute services to the data factory. 
# In this quickstart, we only need create one Azure Storage linked service as both copy source and sink store, named "AzureStorageLinkedService" in the sample. 
# Replace <storageaccountname> and <storageaccountkey> with name and key of our Azure Storage account.

# Create an Azure Storage linked service
    ls_name = 'storageLinkedService001'

    # IMPORTANT: specify the name and key of your Azure Storage account.
    storage_string = SecureString(value='DefaultEndpointsProtocol=https;AccountName=<account name>;AccountKey=<account key>;EndpointSuffix=<suffix>')

    ls_azure_storage = LinkedServiceResource(properties=AzureStorageLinkedService(connection_string=storage_string)) 
    ls = adf_client.linked_services.create_or_update(rg_name, df_name, ls_name, ls_azure_storage)
    print_item(ls)
