import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    driver.get(
        "file:///C:/Users/Zawa and Zaid/Desktop/QA-Selenium/login.html"
    )

    yield driver

    driver.quit()


def login(driver, username, password):
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "submit-login").click()

    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    return message.text


@pytest.mark.parametrize("username,password,expected", [
    ("zacky", "123456", "Login berhasil"),                  # TC-001
    ("zacky", "salah123", "Username atau password salah"),  # TC-002
    ("", "123456", "Username wajib diisi"),                 # TC-003
    ("zacky", "", "Username atau password salah"),          # TC-004
    ("", "", "Username wajib diisi"),                       # TC-005
])
def test_login(driver, username, password, expected):
    message = login(driver, username, password)

    assert message == expected