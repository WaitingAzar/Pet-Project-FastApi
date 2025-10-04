from fastapi import APIRouter
from DataBase import container  # твій Cosmos DB контейнер

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/get_all")
def get_all_products():
    query = "SELECT * FROM c"
    items = list(container.query_items(
        query=query,
        enable_cross_partition_query=True
    ))
    return items
