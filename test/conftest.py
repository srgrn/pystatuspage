import pytest
import pystatuspage
import os

SECRETS_FILE = 'secrets.json'


@pytest.fixture(scope="module")
def secrets():

    if os.path.exists(SECRETS_FILE):
        import json
        with open(SECRETS_FILE) as json_file:
            secrets = json.load(json_file)
    else:
        secrets = {}
        secrets['organization_id'] = os.environ.get('STATUSPAGE_ORG_ID', '12345678')
        secrets['key'] = os.environ.get('STATUSPAGE_API_KEY', 'No Key Found')
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
