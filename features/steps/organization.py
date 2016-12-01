# -*- coding: utf-8 -*-
import re
from ConfigParser import SafeConfigParser

import time
from behave import *
from wheel.signatures import assertTrue
from features.pages.page_selector import LoginPageLocator, HomePageLocator
import general_methods

config = SafeConfigParser()
config.read('settings.ini')
username = config.get('main', 'username')
psw = config.get('main', 'psw')

#Вводимо логін
@when("login ass owner")
def step(context):
    general_methods.login(context,email=username, password=psw)

#Click on My organizatino button
@when("click on My_organization button")
def step(context):
    context.browser.find_element(*HomePageLocator.My_organizations_btn).click()

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