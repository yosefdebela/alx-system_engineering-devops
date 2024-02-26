"""
Validate API key returns "OK" response
"""
import os
from dotenv import load_dotenv
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi
from datadog_api_client.v1.api.authentication_api import AuthenticationApi
load_dotenv()
# Store credentials
pwd = os.getenv('DD_APP_KEY')
key = os.getenv('DD_API_KEY')
DD_SITE="datadoghq.com"

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuthenticationApi(api_client)
    response = api_instance.validate()

    print(response)
