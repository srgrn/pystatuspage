import pytest
import pystatuspage


@pytest.fixture(scope="module")
def secrets():
    import json
    with open("secrets.json") as json_file:
        secrets = json.load(json_file)
    return secrets


@pytest.fixture(scope="module")
def init_statuspage_with_key(secrets):
    organization_id = secrets['organization_id']
    key = secrets['key']
    api = pystatuspage.StatusPageApi(organization_id, key)
    return api


@pytest.fixture(scope="module")
def init_statuspage_without_key(secrets):
    organization_id = secrets['organization_id']
    api = pystatuspage.StatusPageApi(organization_id)
    return api
