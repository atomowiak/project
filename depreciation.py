import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def open_website():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://kalkulatory.gofin.pl/Kalkulator-amortyzacja-metoda-liniowa,12.html")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.find_element_by_id("formalAgreementModalAgree").click()


@pytest.mark.parametrize('input, expected', [('10000', '166,67zł'),('5000', '83,33zł'),('15258,15', '254,30zł')])

def test_amortyzacja(open_website, input, expected):
    driver.find_element_by_id("WartoscPoczatkowaSrodkaTrwalego_input").clear()
    driver.find_element_by_id("WartoscPoczatkowaSrodkaTrwalego_input").send_keys(input)
    driver.find_element_by_id("stawka").send_keys("20")
    driver.find_element_by_id("przyciskObliczenia").click()
    amounts = driver.find_elements_by_xpath("//*[@id='kalkulatorWyniki']/table[1]/tbody/tr[5]/td")
    amounts_value = [amount.get_attribute("textContent") for amount in amounts]
    result = str(amounts_value).replace(" ", "").replace("\\n", "").replace("[", "").replace("]", "").replace("\'", "")

    driver.quit()

    assert expected == result




