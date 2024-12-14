import pytest
from django.test import AsyncClient


@pytest.fixture
def async_client():
    return AsyncClient()
