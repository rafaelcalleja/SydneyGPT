import unittest
from unittest import mock
from unittest.mock import MagicMock

try:
    namespace = 'EdgeGPT.EdgeUtils'
    from EdgeGPT import EdgeUtils
except (ImportError, ModuleNotFoundError):
    namespace = 'EdgeUtils'
    import EdgeUtils

from retry import retry
from SydneyGPT.SydneyGPTUtils import Query


class TestSydneyGPTUtils(unittest.TestCase):
    def test_ask(self):
        response = self.do_query("What are you? Give your answer as Python code")

        self.assertIn("Sydney", response)

    @staticmethod
    @retry(tries=3, delay=2)
    def do_query(query: str):
        with    mock.patch(f"{namespace}.Cookie.import_data", return_value=None), \
                mock.patch(f"{namespace}.Cookie.import_next", return_value=None), \
                mock.patch(f"{namespace}.Cookie.files", return_value=['file1.txt', 'file2.txt']):

            mock_filepath = MagicMock()
            mock_filepath.name = '1'

            EdgeUtils.Cookie.current_data = None
            EdgeUtils.Cookie.current_filepath = mock_filepath

            return Query(query).output

