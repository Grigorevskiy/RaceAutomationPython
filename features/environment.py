import os

from selenium import webdriver

def before_scenario(context, scenario):
    context.browser = webdriver.Chrome(executable_path='{}/chromedriver'.format(os.getcwd()))
    # context.browser = webdriver.Chrome() if you have set chromedriver in your PATH
    context.browser.set_page_load_timeout(10)
    context.browser.implicitly_wait(10)
    context.browser.maximize_window()



def after_scenario(context, scenario):
    context.browser.close()
