from zappa_client import ZappaClient


def test_zappa_client():
    client = ZappaClient()
    assert client is not None