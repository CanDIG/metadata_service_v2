from uuid import uuid4

from django.conf import settings
import requests


def create_or_query_dataset(dataset_id):
    url = settings.DATASET_SERVICE_URL

    if not url:
        raise Exception('Dataset service is not configured properly')

    data = {
        "id": uuid4(),
        "name": dataset_id
    }

    res = requests.post(url, data=data)

    # TODO: hmm I might not have used 405 method not allowed
    # in that context...
    if res.status_code == 405:
        return True

    res.raise_for_status()

    return True
