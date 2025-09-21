from azure.cosmos import CosmosClient
from .config import COSMOS_ENDPOINT, COSMOS_KEY, DATABASE_NAME, CONTAINER_NAME

def get_cosmos_client(endpoint: str, key: str) -> CosmosClient:
    return CosmosClient(endpoint, key, connection_verify=False)

client = get_cosmos_client(COSMOS_ENDPOINT,COSMOS_KEY)
