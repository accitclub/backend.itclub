import pytest
from itc_backend.apps.core.models.executive import Executive, ExecutiveYear
from itc_backend.apps.core.tests.factories import SocialMediaFactory, ExecutivesFactory

pytestmark = pytest.mark.django_db


class TestExecutiveModels:

    def test_social_media_model(self):
        sm = SocialMediaFactory()
        assert sm.name is not None
        assert sm.link is not None

    def test_executive(self):
        executive_year = ExecutiveYear.objects.create(
            title="YEAR-2021",
            year="2021",
        )
        executive_1 = Executive.objects.create(
            name="John Doe",
            post="Admin",
            executive_year=executive_year
        )
        assert executive_1.serial == 0

        executive_2 = Executive.objects.create(
            name="John Don",
            post="Admin",
            executive_year=executive_year
        )
        assert executive_2.serial == 1

    def test_executive_social_media(self):
        _exec = ExecutivesFactory()
        sm = SocialMediaFactory()
        _exec.social_media.add(sm)
        assert _exec.social_media is not None
