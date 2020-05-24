import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def settings():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()


@pytest.fixture(params=[{"input": "1000"},
                        {"input": "15000"}])


def function(request):
        return request.param

def test_tax(settings, function):
    driver.get("https://www.e-pity.pl/kwota-wolna-od-podatku-pit-kalkulator/")
    driver.find_element_by_id("exampleInputAmount").send_keys(function["input"])
    driver.find_element_by_xpath("//button[text()='wylicz']").click()
    tax = driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/div[2]/div[2]/div/h3/strong").text

    assert tax == "ZERO zł"

    driver.quit()



