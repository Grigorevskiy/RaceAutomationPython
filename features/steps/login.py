# -*- coding: utf-8 -*-
import re
from behave import *
import features.steps.registration
import time
#from dbfolder import get_mail
from selenium.common.exceptions import NoSuchElementException

from dbfolder import get_mail
from features.pages.page_selector import LoginPageLocator, HomePageLocator
from features.steps import registration
from features.steps import variables

#----------------------
def _existing_email():
    import csv
    csvfile = open('data.csv', 'rb')
    csvFileArray = []
    for row in csv.reader(csvfile, delimiter=','):
        csvFileArray.append(row)
    em = (csvFileArray[1][2])
    return em
#---------------------
def _check_email_box():

    count = 1

    while (count <= 2):
        time.sleep(1.5)
        count = count + 1
        mail_list = get_mail.get_unread_email()
        regexp = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
        token_link = re.compile(r'http([^"]+)')
        if regexp.search(mail_list).group(0) == _existing_email():
            return True
            f = open("token_list.txt", "rw")
            f.write(token_link.search(mail_list).group(0))
            f.close()
            break

        else:
            continue
#----------------------
def _is_element_present(context, test, test1):
    try:
        context.browser.find_element(test, test1)  # find body tag element
    except NoSuchElementException, e:
        return False
    return True
#----------------------

@given('website "{url}"')
def step(context, url):
    context.browser.get(url)


#Вводимо логін
@when("enter email which was registered")
def step(context):

    context.browser.find_element(*LoginPageLocator.EMAIL_FIELD).send_keys(_existing_email())
    time.sleep(2)

#Вводимо пароль
@when("enter password '{text}'")
def step(context, text):

    context.browser.find_element(*LoginPageLocator.PASSWORD_FIELD).send_keys(text)

#Нажимаэмо на кнопку Sign In
@when("click on button SignIn")
def step(context):

    context.browser.find_element(*LoginPageLocator.SIGNIN_BUTTON).click()

@then("user '{text}' was login successfully")
def step(context, text):

    username = context.browser.find_element(*HomePageLocator.FULLNAME_USER).text
    assert username == text

#Проверим, что мы на странице с результатами поиска, есть некоторый искомый текст
@then("appear validation message '{text}'")
def step(context, text):

    username = context.browser.find_element(*LoginPageLocator.VALIDATION_MESSAGE).text
    time.sleep(2)
    assert username == text

# --------------- FORGOT PASSWORD

@when("click on Forgot link")
def step(context):
    time.sleep(1)
    context.browser.find_element(*LoginPageLocator.FORGOT_LINK).click()
    time.sleep(1)

@then("appears Forgot field")
def step(context):



    assert _is_element_present(context, *LoginPageLocator.EMAIL_FIELD) == True

@when ("enter existing email")
def step(context):
    context.browser.find_element(*LoginPageLocator.EMAIL_FIELD).send_keys(_existing_email())
    time.sleep(1)

@when ("click on Restore button")
def step(context):
    context.browser.find_element(*LoginPageLocator.RESTORE_BUTTON).click()


@then ("email was send on your mail box")
def step(context):

    assert _check_email_box() == True

@when ("click on reset link")
def step(context):
    f = open("token_list.txt", "r")
    restore_url = f.readline()
    f.close()
    context.browser.get(restore_url)

@then ("appears Password restore fields")
def step(context):

    _is_element_present(context, *LoginPageLocator.PASSWORD_FIELD)

@when ("enter new password '{psw}'")
def step(context, psw):
    context.browser.find_element(*LoginPageLocator.PASSWORD_FIELD).send_keys(psw)
    context.browser.find_element(*LoginPageLocator.CONFIRM_PASSWORD).send_keys(psw)

@when("click on Change my password button")
def step(context):
    time.sleep(1)
    context.browser.find_element(*LoginPageLocator.CHANGE_MY_PASSWORD_BUTTON).click()


@then ("should redirect on Login screen")
def step(context):
    time.sleep(1)
    _is_element_present(context, *LoginPageLocator.EMAIL_FIELD)


# @when ("click on Change my password button")
# def step(context):
#     time.sleep(1)
#     context.browser.find_element(*LoginPageLocator.CHANGE_MY_PASSWORD_BUTTON).click()
#     time.sleep(2)
