# Add the following code to the Main method that creates a data factory. 
# If our resource group already exists, comment out the first create_or_update statement

# create the resource group
# comment out if the resource group already exits
resource_client.resource_groups.create_or_update(rg_name, rg_params)

#Create a data factory
df_resource = Factory(location='westus')
df = adf_client.factories.create_or_update(rg_name, df_name, df_resource)
print_item(df)
while df.provisioning_state != 'Succeeded':
    df = adf_client.factories.get(rg_name, df_name)
    time.sleep(1)
