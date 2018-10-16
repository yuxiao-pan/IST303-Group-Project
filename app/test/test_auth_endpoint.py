import pytest

@pytest.mark.urls('news.urls')
def test_index_page(client):
    expected = 'Application news portal Started'
    result = client.get('/').content.decode("utf-8")
    assert expected in result


