from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from datetime import datetime
import os
from testrail_cfg import AddResultForCase, AddRun, TestRailParams
import configparser


config = configparser.ConfigParser()
config.read('run_settings.ini')


# todo: make tests independent by adding login/logout for each test separately
def before_all(context):
    options = Options()
    headless_setting = config['chrome']['headless']
    if headless_setting == 'true':
        options.headless = True
    options.add_argument('disable-gpu')
    context.driver = webdriver.Chrome(chrome_options=options)

    login_page = config['urls']['login_page']
    context.driver.get(login_page)

    if TestRailParams.account_active is True:
        context.run_id = AddRun().get_run_id()


def after_step(context, step):
    if step.status == 'failed':
        filename = context.scenario.name + "_" + datetime.now().strftime('%Y%m%d%H%M%S') + ".png"
        context.driver.save_screenshot((os.path.join(os.path.expanduser('~\\Downloads'), filename)))
        context.driver.switch_to.default_content()



def find_case_id_tag(scenario):
    for tag in scenario.tags:
        if tag.startswith('case_id='):
            return tag[9:]

def after_scenario(context, scenario):
    if TestRailParams.account_active is True:
        status = scenario.status
        case_id = find_case_id_tag(scenario)
        AddResultForCase().send_result(context, status, case_id)
