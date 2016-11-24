from features.pages.page_selector import LoginPageLocator


def login(context, email, password):
    context.browser.find_element(*LoginPageLocator.EMAIL_FIELD).send_keys(email)
    context.browser.find_element(*LoginPageLocator.PASSWORD_FIELD).send_keys(password)
    context.browser.find_element(*LoginPageLocator.SIGNIN_BUTTON).click()