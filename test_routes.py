import unittest
from octokit_routes import specifications
from octokit_routes import webhook_names


class TestRoutes(unittest.TestCase):
    def test_can_import_and_get_verion(self):
        self.assertEqual(specifications['api.github.com']['info']['version'], '9.0.0')


class TestWebhooks(unittest.TestCase):
    def test_can_import_webhooks(self):
        self.assertTrue("*" in webhook_names)