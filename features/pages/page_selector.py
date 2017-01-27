from selenium.webdriver.common.by import By


class LoginPageLocator(object):

    EMAIL_FIELD = (By.ID, 'user_email')
    PASSWORD_FIELD = (By.ID, "user_password")
    SIGNIN_BUTTON = (By.CSS_SELECTOR, ".btn.btn-green.sign-submit")
    VALIDATION_MESSAGE = (By.CSS_SELECTOR, ".message")
    FORGOT_LINK = (By.CSS_SELECTOR, ".sign-block>a")
    RESTORE_BUTTON = (By.CSS_SELECTOR, ".btn.btn-green.sign-submit")
    CHANGE_MY_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".btn.btn-green.change-submit")
    CONFIRM_PASSWORD = (By.ID, 'user_password_confirmation')

class RegistrationPageLocator(object):

    SIGNIN_TAB = (By.XPATH, "//a[@href='#signUp']")
    FIRST_NAME = (By.ID, "user_first_name")
    LAST_NAME = (By.ID, "user_last_name")
    EMAIL_FIELD = (By.ID, "registration_user_email")
    COMPANY_FIELD = (By.ID, "user_company")
    COUNTRY_FIELD = (By.XPATH, ".//a[.='Ukraine']")
    PASSWORD_FIELD = (By.XPATH, "//form[@id='new_user_registration']/div[6]/input")
    CONF_PASS = (By.ID, "user_password_confirmation")
    SIGNUP_BUTTON = (By.XPATH, "//input[@value='Sign up']")

class HomePageLocator(object):

    FULLNAME_USER = (By.CSS_SELECTOR, ".username")
    My_organizations_btn = (By.XPATH, ".//ul[@class='main_tabs']/li[1]/a")
    Create_new_organization_btn = (By.XPATH, "//*[contains(text(),'Create new organization')]")
    Add_new_organization_btn = (By.XPATH, ".//input[@value='Add New Organization']")


class OrganizationPopup(object):
    TITLE = (By.ID, "organization_title")
    DESC = (By.ID, "organization_description")
    SUBMIT = (By.XPATH, ".//input[@value='Add New Organization']")
    SAVE_CHANGES = (By.XPATH, ".//input[@value='Save changes']")
    ORG_NAME = (By.CSS_SELECTOR, ".organization-name")
    CHANGE_BTN = (By.XPATH, "//*[contains(text(),'Change')]")
    MY_ORG_LEFT_MENU = (By.XPATH, "//div[@id='left-menu']//li[3]")
    #DELETE
    DEL_ORG_LEFT_MENU = (By.XPATH, "//div[@id='organizations-left-menu']//li[6]")
    DEL_ORG_CONFIRM = (By.CSS_SELECTOR, ".btn.btn-red.card-header-btn.open_popup")
    DEL_ORG_CONFIRM2 = (By.ID, "#confirm")
    ORGS_COUNT = (By.XPATH, "//div[@class='columns-wrapper']/div")
