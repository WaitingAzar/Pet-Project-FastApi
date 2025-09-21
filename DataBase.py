from azure.cosmos import CosmosClient, PartitionKey
from config import COSMOS_ENDPOINT, COSMOS_KEY, DATABASE_NAME, CONTAINER_NAME

client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)

# База даних
database = client.create_database_if_not_exists(id=DATABASE_NAME)

# Контейнер з правильним partition key
container = database.create_container_if_not_exists(
    id=CONTAINER_NAME,
    partition_key=PartitionKey(path="/taskId"),  # partition key окремо від id
    offer_throughput=400
)
