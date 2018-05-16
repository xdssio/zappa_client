from zappa_client import ZappaClient


def test_zappa_client():
    """
    TODO
    :return:
    """
    client = ZappaClient()
    assert client is not None
