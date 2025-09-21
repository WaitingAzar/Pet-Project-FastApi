from azure.cosmos import CosmosClient
from .config import COSMOS_ENDPOINT, COSMOS_KEY, DATABASE_NAME, CONTAINER_NAME

def get_cosmos_client(endpoint: str, key: str) -> CosmosClient:
    return CosmosClient(endpoint, key, connection_verify=False)

# Створюємо клієнта
client = get_cosmos_client(COSMOS_ENDPOINT, COSMOS_KEY)

# Створюємо базу даних, якщо не існує
database = client.create_database_if_not_exists(id=DATABASE_NAME)

# Створюємо контейнер, якщо не існує
container = database.create_container_if_not_exists(
    id=CONTAINER_NAME,
    partition_key="/id"
)
