import product_api
from unittest import TestCase
from unittest.mock import patch


class TestProductApi(TestCase):

    # Patch get_products and test lambda_handler returns a single record
    @patch('product_api.get_products')
    def test_lambda_handler_single(self, mock_get_products):
        mock_get_products.return_value = [
            {'id': '1', 'name': 'test', 'description': 'test'}
            ]
        response = product_api.lambda_handler(None, None)
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(
            response['body'],
            '[{"id": "1", "name": "test", "description": "test"}]'
            )

    # Patch get_products and test lambda_handler returns a multiple records
    @patch('product_api.get_products')
    def test_lambda_handler_multiple(self, mock_get_products):
        mock_get_products.return_value = [
            {'id': '1', 'name': 'test', 'description': 'test'},
            {'id': '2', 'name': 'test2', 'description': 'test2'}
            ]
        response = product_api.lambda_handler(None, None)
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(
            response['body'],
            '[{"id": "1", "name": "test", "description": "test"}, '
            '{"id": "2", "name": "test2", "description": "test2"}]'
            )
