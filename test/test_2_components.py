import pytest
import pystatuspage


class TestComponents(object):

    def test_get_components_with_key(self, init_statuspage_with_key):
        api = init_statuspage_with_key
        components = api.get_all_components()
        assert len(components) > 0
        assert isinstance(components[0], pystatuspage.StatusPageComponent)

    def test_update_component_with_key(self, init_statuspage_with_key):
        api = init_statuspage_with_key
        components = api.get_all_components()
        assert components[0].status == pystatuspage.StatusPageComponent.OPERATIONAL
        api.update_component(components[0], pystatuspage.StatusPageComponent.MAJOR_OUTAGE)
        components = api.get_all_components()
        assert components[0].status == pystatuspage.StatusPageComponent.MAJOR_OUTAGE
        api.update_component(components[0], pystatuspage.StatusPageComponent.OPERATIONAL)
        components = api.get_all_components()
        assert components[0].status == pystatuspage.StatusPageComponent.OPERATIONAL

    @pytest.mark.public
    def test_get_components_without_key(self, init_statuspage_without_key):
        api = init_statuspage_without_key
        components = api.get_all_components()
        assert len(components) > 0
        assert isinstance(components[0], pystatuspage.StatusPageComponent)
