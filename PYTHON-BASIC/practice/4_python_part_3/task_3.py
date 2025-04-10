"""
Write a function which detects if entered string is http/https domain name with optional slash at the and
Restriction: use re module
Note that address may have several domain levels
    >>>is_http_domain('http://wikipedia.org')
    True
    >>>is_http_domain('https://ru.wikipedia.org/')
    True
    >>>is_http_domain('griddynamics.com')
    False
"""
import re

def is_http_domain(domain: str) -> bool:
    pattern = r"^https?://([\w.-]+\.)?[\w-]+\.\w+/?$"
    return bool(re.match(pattern, domain))


"""
write tests for is_http_domain function
"""
from regex import is_http_domain

def test_valid_http():
    assert is_http_domain("http://example.com") is True

def test_valid_https_with_subdomain_and_slash():
    assert is_http_domain("https://sub.example.co.uk/") is True

def test_missing_protocol():
    assert is_http_domain("example.com") is False

def test_invalid_format():
    assert is_http_domain("ftp://example.com") is False

def test_http_with_multiple_subdomains():
    assert is_http_domain("http://deep.sub.domain.org") is True
