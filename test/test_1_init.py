import pytest
import pystatuspage


class TestInitializaion(object):

    def test_init_with_key(self, secrets):
        organization_id = secrets['organization_id']
        key = secrets['key']
        api = pystatuspage.StatusPageApi(organization_id, key)
        assert api._public_url == "https://" + organization_id + ".statuspage.io/api/v2/"
        assert hasattr(api, '_oauth_token')
        assert api._oauth_token is key

    @pytest.mark.public
    def test_init_witout_key(self, secrets):
        organization_id = secrets['organization_id']
        api = pystatuspage.StatusPageApi(organization_id)
        assert api._public_url == "https://" + organization_id + ".statuspage.io/api/v2/"
        assert not hasattr(api, '_oauth_token')
