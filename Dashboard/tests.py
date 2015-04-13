import pytest

@pytest.mark.django_db
class TestViews:

    def test_home_view(self, client):
        response = client.get('/')
        assert response.status_code == 200


    def test_saftey_view(self, client):
        response = client.get('/safety', follow=True)
        assert response.status_code == 200

    def test_economic_view(self, client):
        response = client.get('/economic', follow=True)
        assert response.status_code == 200

    def test_civic_view(self, client):
        response = client.get('/civic', follow=True)
        assert response.status_code == 200

    def test_governement_view(self, client):
        response = client.get('/government', follow=True)
        #print (response.content, end=" ")
        assert response.status_code == 200