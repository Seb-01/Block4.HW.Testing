import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    """ APIClient foe tests """
    return APIClient()