from datastore.datastore import DataStore
import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

async def get_datastore() -> DataStore:
    datastore = os.getenv("DATASTORE")
    assert datastore is not None

    match datastore:
        case "pinecone":
            from datastore.providers.pinecone_datastore import PineconeDataStore

            return PineconeDataStore()
        case "weaviate":
            from datastore.providers.weaviate_datastore import WeaviateDataStore

            return WeaviateDataStore()
        case "milvus":
            from datastore.providers.milvus_datastore import MilvusDataStore

            return MilvusDataStore()
        case "zilliz":
            from datastore.providers.zilliz_datastore import ZillizDataStore

            return ZillizDataStore()
        case "redis":
            from datastore.providers.redis_datastore import RedisDataStore

            return await RedisDataStore.init()
        case "qdrant":
            from datastore.providers.qdrant_datastore import QdrantDataStore

            return QdrantDataStore()
        case _:
            raise ValueError(f"Unsupported vector database: {datastore}")
