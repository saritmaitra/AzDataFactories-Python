# Install the Python package 
# terminal or command prompt with administrator privileges. 

pip install azure-mgmt-resource # package for Azure management resources
pip install azure-mgmt-datafactory # package for Data Factory
pip install azure-identity # package for Azure Identity authentication

# data factory client
# Create a file named datafactory.py. Add the following statements to add references to namespaces.
from azure.identity import ClientSecretCredential 
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import *
from datetime import datetime, timedelta
import time


