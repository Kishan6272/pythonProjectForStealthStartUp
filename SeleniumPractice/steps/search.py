from behave import *

@given(u'I got navigated to home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I got navigated to home page')


@when(u'I enter a valid product in the Search box field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter a valid product in the Search box field')


@when(u'I click on Search button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on Search button')


@then(u'Valid product should get displayed in the Search results')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Valid product should get displayed in the Search results')


@when(u'I enter a invalid product in the Search box field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter a invalid product in the Search box field')


@then(u'inValid product should not get displayed in the Search results')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then inValid product should not get displayed in the Search results')


@when(u'I  dont enter anything into the Search box field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I  dont enter anything into the Search box field')


@then(u'Proper message should  displayed in the Search results')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Proper message should  displayed in the Search results')
