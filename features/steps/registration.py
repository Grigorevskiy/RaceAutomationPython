import time
from behave import given, when, then

#from dbfolder.writeToFile import write_to_file
from features.pages.page_selector import RegistrationPageLocator, HomePageLocator, LoginPageLocator

def _generate_mail(email):
    split_email = email.split('@')
    import rstr as rstr
    random1 = rstr.xeger(r'\d\d\d\d\d')
    return split_email[0]+'+'+str(random1)+'@'+split_email[1]


@given('websitee "{url}"')
def step(context, url):
    context.browser.get(url)


@when("click on Sign up tab")
def step(context):
    context.browser.find_element(*RegistrationPageLocator.SIGNIN_TAB).click()

@when("fill registration form '{first_name}', '{last_name}', '{email}', '{company}', '{country}', '{password}'")
def step(context, first_name, last_name, email, company, country, password):

    context.browser.find_element(*RegistrationPageLocator.FIRST_NAME).send_keys(first_name)
    context.browser.find_element(*RegistrationPageLocator.LAST_NAME).send_keys(last_name)
    testmail = _generate_mail(email)
    context.browser.find_element(*RegistrationPageLocator.EMAIL_FIELD).send_keys(testmail)
    context.browser.find_element(*RegistrationPageLocator.COMPANY_FIELD).send_keys(company)
    time.sleep(0.5)
    dropdown = context.browser.find_element_by_css_selector(".dd-selected")
    dropdown.click()
    context.browser.find_element_by_xpath(".//a[.='{}']".format(country)).click()
    context.browser.find_element(*RegistrationPageLocator.PASSWORD_FIELD).send_keys(password)
    context.browser.find_element(*RegistrationPageLocator.CONF_PASS).send_keys(password)

    write_to_file(first_name, last_name, testmail, company)

@when("fill email field '{email}'")
def step(context, email):
    context.browser.find_element(*RegistrationPageLocator.EMAIL_FIELD).send_keys(email)

@when("click on button SignUp")
def step(context):

    context.browser.find_element(*RegistrationPageLocator.SIGNUP_BUTTON).click()

@then("user '{text}' was register successfully")
def step(context, text):
    time.sleep(1)
    username = context.browser.find_element(*HomePageLocator.FULLNAME_USER).text
    assert username == text
    #context.browser.save_screenshot('{}/Registration/screenshots/registration_successfully.png'.format(project_dir))

@then("appear validation messages '{text1}'")
def step(context, text1):

    valid_message = context.browser.find_element(*LoginPageLocator.VALIDATION_MESSAGE).text
    time.sleep(0.5)
    assert valid_message == text1

    #context.browser.save_screenshot('{}/Loginization/screenshots/{}.png'.format(project_dir, {str(text)}))
    # context.browser.quit()

