# CanDIGv2 Metadata Service

This application contains the metadata-related models from CanDIG v1, reorganized
as a micro-service build with Django and offering GraphQL querying capacities.

## Development setup

Development dependencies are described in `requirements.txt` and can be
installed using the following command:

```bash
pip install -r requirements.txt
```

Currently, the DB is included in the repo. To start the server:

```bash
./manage.py runserver
```

## Extract the GraphQL schema

graphene-django provides us with this command line tool to extract
the GraphQL schema defined in this application.

```bash
./manage.py graphql_schema --schema candig_metadata.candig.schema.schema --out schema.graphql
```

Currently, to integrate this schema into the search micro-service, one has to rename the types
without the suffix "Type" appended. A similar process is to be employed with nested objects,
sampleSet becomes samples. WIP
