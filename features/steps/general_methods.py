import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from wheel.signatures import assertTrue

from features.pages.page_selector import LoginPageLocator, OrganizationPopup, HomePageLocator
from selenium.webdriver.support import expected_conditions as EC

def login(context, email, password):
    context.browser.find_element(*LoginPageLocator.EMAIL_FIELD).send_keys(email)
    context.browser.find_element(*LoginPageLocator.PASSWORD_FIELD).send_keys(password)
    context.browser.find_element(*LoginPageLocator.SIGNIN_BUTTON).click()


# Organization
def clear_organizations(context):
    listtt = len(context.browser.find_elements(*OrganizationPopup.ORGS_COUNT))
    if listtt != 0:
        for i in range(listtt):
            time.sleep(1)
            context.browser.find_element(By.XPATH, "//div[@class='columns-wrapper']/div[1]//a[@class='organization-name']").click()
            time.sleep(0.5)
            context.browser.find_element(By.XPATH, ".//span[text()='Delete organization']").click()
            time.sleep(0.5)
            context.browser.find_element(By.XPATH, ".//a[text()='Delete organization']").click()
            time.sleep(0.5)
            context.browser.find_element(By.XPATH, ".//a[text()='Delete']").click()
            time.sleep(1.5)
    else:
        print ("List is empty")

def create_organization(context, name):
    context.browser.find_element(*HomePageLocator.My_organizations_btn).click()
    time.sleep(1)
    btn = context.browser.find_element(*HomePageLocator.Create_new_organization_btn)
    assertTrue(btn)
    context.browser.find_element(*HomePageLocator.Create_new_organization_btn).click()
    time.sleep(5)
    context.browser.find_element(*OrganizationPopup.TITLE).send_keys(name)
    context.browser.find_element(*OrganizationPopup.DESC).send_keys("Test organization")
    context.browser.find_element(*OrganizationPopup.SUBMIT).click()
    time.sleep(1)