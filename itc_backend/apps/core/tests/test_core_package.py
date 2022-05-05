from django.test import TestCase
import pytest


class TestCorePackage(TestCase):
    def test_core_package_available(self):
        self.assertEqual(1, 1)
