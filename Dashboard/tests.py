import pytest, py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User

ADMIN_USERNAME = "ikani"
ADMIN_PASSWORD = "ikani"

class TestSelenium:

    def test_admin_login(self):

        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/admin")
        assert "Log in" in driver.title
        usernameElem = driver.find_element_by_name("username")
        usernameElem.send_keys(ADMIN_USERNAME)
        passwordElem = driver.find_element_by_name("password")
        passwordElem.send_keys(ADMIN_USERNAME)
        passwordElem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
#        assert "Site administration" in driver.title
        driver.close()

    """
    SQL injection code can go here, and we can expect failure, or appearance of the alert messages
    """
    def test_sql_injection(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/admin")
        assert "Log in" in driver.title
        usernameElem = driver.find_element_by_name("username")
        usernameElem.send_keys(ADMIN_USERNAME)
        passwordElem = driver.find_element_by_name("password")
        passwordElem.send_keys(ADMIN_USERNAME)
        passwordElem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
#        assert "Site administration" in driver.title
        driver.close()



@pytest.mark.django_db
class TestViews:

    # pytestmark = pytest.mark.django_db
    # def test_my_user(self):
    #     me = User.objects.get(username='ikani')
    #     assert me.is_superuser

    # def test_admin_login(self, client):
    #     response = client.post('/login/', {'username': 'ikani', 'password': 'ikani'})
    #     assert response.status_code == 200


    def test_an_admin_view(self, admin_client):
        response = admin_client.get('/admin/')
        assert response.status_code == 200

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

    def test_invalid_url(self, client):
        response = client.get('/error')
        assert response.status_code == 404


class TestExamples:

    # Expecting an exception example
    def test_zero_division(slef):
        with pytest.raises(ZeroDivisionError):
            1 / 0