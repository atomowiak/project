import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def open_website():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://kalkulatory.gofin.pl/Kalkulator-amortyzacja-metoda-liniowa,12.html")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.find_element_by_id("formalAgreementModalAgree").click()
    return driver



@pytest.mark.parametrize('input, expected', [('10000', '166,67 zł'),('5000', '83,33 zł'),('15258,15', '254,30 zł')])

def test_amortyzacja(open_website, input, expected):
    driver = open_website
    driver.find_element_by_id("WartoscPoczatkowaSrodkaTrwalego_input").clear()
    driver.find_element_by_id("WartoscPoczatkowaSrodkaTrwalego_input").send_keys(input)
    driver.find_element_by_id("stawka").send_keys("20")
    driver.find_element_by_id("przyciskObliczenia").click()
    amounts = driver.find_element_by_xpath("//*[@id='kalkulatorWyniki']/table[1]/tbody/tr[5]/td").text
    result = str(amounts).strip()

    driver.quit()

    assert expected == result




