# -*- coding: utf-8 -*-
import re
from behave import *
from wheel.signatures import assertTrue

import features.steps.registration
import time
from dbfolder import get_mail
from selenium.common.exceptions import NoSuchElementException

from features.pages.page_selector import LoginPageLocator, HomePageLocator
from features.steps import registration
from features.steps import variables
import general_methods

#Вводимо логін
@when("login ass '{email}','{password}'")
def step(context, email, password):
    general_methods.login(context,email=email, password=password)

#Click on My organizatino button
@when("click on My_organization button")
def step(context):
    context.browser.find_element(*HomePageLocator.My_organizations_btn).click()

@then("appear button Create_new_organization button")
def step(context):
    btn = context.browser.find_element(*HomePageLocator.Create_new_organization_btn)
    assertTrue(btn)