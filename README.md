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
