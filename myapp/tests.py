from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


class MySeleniumTests(StaticLiveServerTestCase):
    # Carregar una base de dades de test
    # fixtures = ['testdb.json',]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        opts = Options()
        cls.selenium = WebDriver(options=opts)
        cls.selenium.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        # Anar a la pàgina de login
        self.selenium.get("%s%s" % (self.live_server_url, "admin/login"))
        # Comprova el títol
        self.assertEqual(self.selenium.title, "Log in | Django site admin")
        # Introduim dades de login i fem click al botó login
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys("mkl")
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys("3112")

        self.selenium.find_element(By.XPATH, '//input[@value="Log in"]').click()

        # Test --> mirem si ens trobem a la pàgina d'administració
        self.assertEqual(self.selenium.title, "Site administration | Django site admin")
