from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)


class VectorStore:

    def __init__(self):

        self.client = QdrantClient(
            path="./qdrant_data"
        )

        self.collection_name = "documents"

        self.create_collection()


    def create_collection(self):

        collections = (
            self.client
            .get_collections()
            .collections
        )

        existing_names = [
            collection.name
            for collection in collections
        ]

        if self.collection_name not in existing_names:

            self.client.create_collection(
                collection_name=self.collection_name,

                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE
                )
            )

            print("Collection created!")

        else:

            print("Collection already exists!")


    def add_vector(
        self,
        vector,
        text,
        vector_id: int,
        metadata=None
    ):

        payload = {
            "text": text
        }

        if metadata:
            payload.update(metadata)

        point = PointStruct(
            id=vector_id,
            vector=vector,
            payload=payload
        )

        self.client.upsert(
            collection_name=self.collection_name,
            points=[point]
        )

        print(
            f"Vector {vector_id} stored successfully!"
        )


    def search(
        self,
        query_vector,
        limit=3
    ):

        results = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=limit
        )

        return results.points