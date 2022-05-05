import pytest
from django.test import RequestFactory

from itc_backend.apps.core.api.executive_api import ExecutiveRetrieveAPI

pytestmark = pytest.mark.django_db


class TestExecutiveAPI:

    def test_executive_api(self, rf: RequestFactory):
        view = ExecutiveRetrieveAPI()
        resp = view.get(rf)
        assert resp is not None
