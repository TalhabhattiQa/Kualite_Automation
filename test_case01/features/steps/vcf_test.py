import configparse
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from vcf_pom import cycle


@given(u'launch chrome and Visit Url')
def launch_url(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)


@when(u'Screen Creation by using valid login credentials')
def screen_creation(context):
    object_cycle = cycle(context.driver)
    object_cycle.creation_screen()


@when(u'Creating first cycle by filling required fields')
def first_cycle(context):
    object_cycle1 = cycle(context.driver)
    object_cycle1.testcase1_mod1()


@When(u'Verify Cycle1 created is available')
def verification1(context):
    object_cycle2 = cycle(context.driver)
    object_cycle2.verify_cycle1()


@when(u'Creating second cycle by filling required fields')
def second_module(context):
    object_cycle3 = cycle(context.driver)
    object_cycle3.testcase1_mod2()


@When(u'Verify Cycle2 is not created')
def verification2(context):
    object_cycle4 = cycle(context.driver)
    object_cycle4.verify_cycle2()


@when(u'Create cycle without entering name and assign to fields')
def third_mod(context):
    object_cycle5 = cycle(context.driver)
    object_cycle5.testcase1_mod3()


@Then(u'Verify User not able to create cycle')
def verification3(context):
    object_cycle6 = cycle(context.driver)
    object_cycle6.verify_mod3()


@when(u'Creating Cycle by filling specific fields')
def fifth_mod(context):
    object_cycle7 = cycle(context.driver)
    object_cycle7.testcase1_mod5()


@when(u'Verify Email sent to assigned user')
def verification5(context):
    object_cycle8 = cycle(context.driver)
    object_cycle8.verify_mod5()


@Then(u'Verify the shown entries on cycle page')
def sixth_mod(context):
    object_cycle9 = cycle(context.driver)
    object_cycle9.testcase_mod7()


@then(u'Varify the search functionality')
def eight_mod(context):
    object_cycle10 = cycle(context.driver)
    object_cycle10.testcase_mod8_name()


@when(u'Click on Copy button')
def ninth_mod(context):
    object_cycle11 = cycle(context.driver)
    object_cycle11.testcase_mod9()


@then(u'Verify the Pop up text')
def verify_ninth(context):
    object_cycle12 = cycle(context.driver)
    object_cycle12.popup_verify()


@when(u'Delete the record')
def tenth_mod(context):
    object_cycle13 = cycle(context.driver)
    object_cycle13.testcase_mod10()


@then(u'Verify that record deleted')
def verify_tenth(context):
    object_cycle14 = cycle(context.driver)
    object_cycle14.delete_verify()


@when(u'Cancel the delete record pop up')
def eleven_mod(context):
    object_cycle15 = cycle(context.driver)
    object_cycle15.testcase_mod11()


@then(u'Verify that record not deleted')
def verify_cancel(context):
    object_cycle16 = cycle(context.driver)
    object_cycle16.cancel_verify()


@then(u'Varify Pagination button')
def twe_mod(context):
    object_cycle17 = cycle(context.driver)
    object_cycle17.testcase_mod12()


