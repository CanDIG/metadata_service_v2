from uuid import uuid4

from django.conf import settings
import requests


def create_or_query_dataset(dataset_id):
    url = f"{settings.DATASET_SERVICE_URL}/v2/datasets"

    if not url:
        raise Exception('Dataset service is not configured properly')

    # TODO: Actually implement authorization ASAP please
    headers = {
        'Authorization': 'not enforced currently'
    }

    data = {
        "id": str(uuid4()),
        "name": dataset_id
    }

    res = requests.post(url, headers=headers, json=data)

    # TODO: hmm I might not have used 405 method not allowed
    # in that context...
    if res.status_code == 405:
        return True

    res.raise_for_status()

    return True


def query_authorization_level(token, dataset):
    # let's pretend we get these from the token
    issuer = 'https://candigauth.calculquebec.ca/auth/realms/candig'
    username = 'poq'

    url = f"{settings.AUTHZ_SERVICE_URL}/authz?issuer={issuer}&username={username}"

    res = requests.get(url)

    res.raise_for_status()
    perms = res.json()

    if dataset in perms:
        return perms[dataset]
    else:
        return 0
