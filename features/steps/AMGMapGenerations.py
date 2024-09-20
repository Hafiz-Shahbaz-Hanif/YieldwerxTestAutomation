import time

from behave import *
from Pages.AMGMapGenerationsPage import AMGMapGenerationsClass
from Pages.ActionsPage import ActionsClass
from Pages.DashboardPage import DashboardClass

actions = ActionsClass()
dc = DashboardClass()
amg_gen = AMGMapGenerationsClass()


@when('Navigate to "Assembly Map Generations" module')
def step_impl(context):
    dc.click_assembly_map_generations_heading(context)


@when('Assembly Map generations module have two sections, "{amg_policies}" and "{generations}" section')
def step_impl(context, amg_policies, generations):
    amg_gen.verify_amg_policies_section_title(context)
    amg_gen.verify_generations_title(context)


@then('Verify that Assembly map policies section contain all the active processed policies list')
def step_impl(context):
    actions.verify_amg_policy_display_on_generations_tab(context)


@then('Verify that Grid contains Name, version, type, facility, work center, device, test program, date modified, successful, failed and pending columns are available')
def step_impl(context):
    amg_gen.verify_amg_policy_section_column_titles(context)
    actions.logout(context)

