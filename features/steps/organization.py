# -*- coding: utf-8 -*-
import re
from ConfigParser import SafeConfigParser

import time
from telnetlib import EC

from behave import *
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from wheel.signatures import assertTrue
from features.pages.page_selector import LoginPageLocator, HomePageLocator, OrganizationPopup
import general_methods

config = SafeConfigParser()
config.read('settings.ini')
username = config.get('main', 'username')
psw = config.get('main', 'psw')

#Вводимо логін
@when("login ass owner")
def step(context):
    time.sleep(2)
    general_methods.login(context,email=username, password=psw)
    time.sleep(1)

#Click on My organizatino button
@when("click on My_organization button")
def step(context):
    time.sleep(2)
    context.browser.find_element(*HomePageLocator.My_organizations_btn).click()
    time.sleep(1)

@then("appear button Create_new_organization button")
def step(context):
    btn = context.browser.find_element(*HomePageLocator.Create_new_organization_btn)
    assertTrue(btn)


@when("click on button 'Create_new_organization'")
def step_impl(context):
    context.browser.find_element(*HomePageLocator.Create_new_organization_btn).click()
    time.sleep(5)

@when('click on "Add New Organization"')
def step_impl(context):
    context.browser.find_element(*HomePageLocator.Add_new_organization_btn).click()


@then('appear validation message "{text1}"')
def step_impl(context, text1):
    valid_message = context.browser.find_element(*LoginPageLocator.VALIDATION_MESSAGE).text
    time.sleep(0.5)
    assert valid_message == text1


@when('create organization "{text1}" and Description "{text2}"')
def step_impl(context, text1, text2):
    time.sleep(2)
    context.browser.find_element(*OrganizationPopup.TITLE).send_keys(text1)
    context.browser.find_element(*OrganizationPopup.DESC).send_keys(text2)
    context.browser.find_element(*OrganizationPopup.SUBMIT).click()



@then('My organization list contain "{text}" organization')
def step_impl(context, text):
    time.sleep(1)
    my_org = context.browser.find_elements(*OrganizationPopup.ORG_NAME)
    time.sleep(1)
    org_list=[]
    for i in my_org:
        org_list.append(i.text)


    if text in org_list:
        assert True
    else:
        assert False


@when("click on Change button")
def step_impl(context):
    context.browser.find_element(*OrganizationPopup.CHANGE_BTN).click()


@when('edit organization "{text1}" and Description "{text2}"')
def step_impl(context, text1, text2):
    context.browser.find_element(*OrganizationPopup.TITLE).clear()
    context.browser.find_element(*OrganizationPopup.TITLE).send_keys(text1)
    context.browser.find_element(*OrganizationPopup.DESC).clear()
    context.browser.find_element(*OrganizationPopup.DESC).send_keys(text2)


@when("click on Save changes button")
def step_impl(context):
    context.browser.find_element(*OrganizationPopup.SAVE_CHANGES).click()
    time.sleep(1)


@when("click on My organization in Left Menu")
def step_impl(context):
    context.browser.find_element(*OrganizationPopup.MY_ORG_LEFT_MENU).click()
    time.sleep(1)


@when("click on organization")
def step_impl(context):
    context.browser.find_element(*OrganizationPopup.ORG_NAME).click()
    time.sleep(1)


@when('click on organization "{text}"')
def step_impl(context, text):
    time.sleep(1)
    context.browser.find_element(By.XPATH, ".//a[text() = '{}']".format(text)).click()


@when('click on "{text}" button in left menu')
def step_impl(context,text):
    context.browser.find_element(By.XPATH, ".//span[text()='{}']".format(text)).click()


@when('click on "{text}" button')
def step_impl(context,text):
    context.browser.find_element(By.XPATH, ".//a[text()='{}']".format(text)).click()


@then('appears popup window "{text}"')
def step_impl(context, text):
    title = context.browser.find_element(By.CSS_SELECTOR, ".title-main>h3").text
    time.sleep(2)
    assertTrue(text, title)



@when('click on "{text}" button in popup')
def step_impl(context,text):
    context.browser.find_element(By.XPATH, ".//a[text()='{}']".format(text)).click()


@then('My organization list not contain "{text}" organization')
def step_impl(context, text):
    time.sleep(1)
    try:
        my_org = context.browser.find_element(*OrganizationPopup.ORG_NAME).text
        time.sleep(1)
        if text is not my_org:
            assert True
        else:
            assert False

    except NoSuchElementException:
        print ("No element")
        assert True


@when("clear all organization")
def step_impl(context):
    general_methods.clear_organizations(context)


@when('create organization "Test one edit"')
def step_impl(context):
    general_methods.create_organization(context, "Test one edit")


@then("just")
def step_impl(context):
    general_methods.wait_on_element(context, "By.XPATH",
                                    ".//div[@class='modal-content container']/div[@class='title-main']/h3[text()[contains(.,'Add Organization Members')]]")