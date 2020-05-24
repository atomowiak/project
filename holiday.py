import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def pytest_generate_tests(metafunc):
    if "start_day" in metafunc.fixturenames:
        metafunc.parametrize("start_day", ["1", "31"])
    if "start_month" in metafunc.fixturenames:
        metafunc.parametrize("start_month", ["Styczeń", "Kwiecień"])
    if "end_day" in metafunc.fixturenames:
        metafunc.parametrize("end_day", ["1", "31"])
    if "end_month" in metafunc.fixturenames:
        metafunc.parametrize("end_month", ["Maj"])

@pytest.fixture
def settings():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


def test_website(settings, start_day, start_month, end_day, end_month):
    driver = settings
    driver.get("https://kalkulatory.gofin.pl/Kalkulator-urlopu-wypoczynkowego-za-czesc-roku-ze-wzgledu-na-okres-pracy.html")
    driver.find_element_by_id("formalAgreementModalAgree").click()
    driver.find_element_by_name("okres-zatrudnienia-odDzien").send_keys(start_day)
    driver.find_element_by_name("okres-zatrudnienia-odMiesiac").send_keys(start_month)
    driver.find_element_by_name("okres-zatrudnienia-doDzien").send_keys(end_day)
    driver.find_element_by_name("okres-zatrudnienia-doMiesiac").send_keys(end_month)
    driver.find_element_by_id("przyciskObliczenia").click()
    days = driver.find_element_by_xpath("//*[@id='kalkulatorWyniki']/table/tbody/tr[6]/td[2]").text

    assert days == "11"

    driver.quit()
