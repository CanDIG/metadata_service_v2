import graphene

import candig_metadata.metadata.schema


class Query(candig_metadata.metadata.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
