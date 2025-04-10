"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     >>> make_request('https://www.google.com')
     200, 'response data'
"""
from typing import Tuple
from urllib import request

def make_request(url: str) -> Tuple[int, str]:
    with request.urlopen(url) as response:
        status_code = response.getcode()  # status code like 200, 404, etc.
        data = response.read().decode('utf-8')  # raw bytes converted to a string
        return status_code, data


"""
Write test for make_request function
Use Mock for mocking request with urlopen https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 200
    >>> m.method2.return_value = b'some text'
    >>> m.method()
    200
    >>> m.method2()
    b'some text'
"""
import pytest
from unittest.mock import MagicMock, patch
from urllib import request
from url_request import make_request  # Replace with actual module name

def test_make_request():
    mock_response = MagicMock()
    mock_response.getcode.return_value = 200
    mock_response.read.return_value = b'Some fake data'
    
    mock_urlopen = MagicMock()
    mock_urlopen.__enter__.return_value = mock_response

    with patch('urllib.request.urlopen', return_value=mock_urlopen):
        status, data = make_request('https://example.com')
        
        assert status == 200
        assert data == 'Some fake data'

