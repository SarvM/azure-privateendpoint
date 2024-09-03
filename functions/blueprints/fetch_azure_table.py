from azure.functions import HttpRequest, HttpResponse
from azure.data.tables import TableServiceClient, TableClient
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import azure.functions as func
import logging
import requests

app_fetch_aztables = func.Blueprint()


@app_fetch_aztables.route(route="fetch-aztables", methods=["GET"])
def fetch_aztables(req: HttpRequest) -> HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    KEY_VAULT_URL = "https://kv-pep-validation.vault.azure.net/"
    # Initialize the Azure Key Vault client
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KEY_VAULT_URL, credential=credential)

    # Fetch all entities from the table
    entities = []
    try:
        secret = client.get_secret("storage-connectionstring")
        secret_value = secret.value

        # Initialize Table Client
        table_client = TableClient.from_connection_string(conn_str=secret_value, table_name="samplefile")
    
        for entity in table_client.list_entities():
            entities.append(entity)
    except Exception as e:
        logging.error(f"Error fetching data from Azure Table: {e}")
        return func.HttpResponse(f"Error fetching data: {e}", status_code=500)

    # Return the entities as JSON
    return func.HttpResponse(
        body=str(entities),
        mimetype="application/json",
        status_code=200
    )