from api4jenkins import Jenkins
import os
from dotenv import load_dotenv
import time
import sys

load_dotenv()

JENKINS_URL = os.getenv('JENKINS_URL')
JENKINS_USERNAME = os.getenv('JENKINS_USERNAME')
JENKINS_PASSWORD = os.getenv('JENKINS_PASSWORD')

JOB_NAMES = [
    '01_DEPLOY_SALES_API',
    '02_DEPLOY_SQS_RECEIVER',
    '03_DEPLOY_GAFL_WEBAPP_PUBLIC',
    '04_DEPLOY_GAFL_WEBAPP_ADMIN',
    '05_DEPLOY_POCL_JOB',
    '06_DEPLOY_FULFILMENT_JOB',
    '07_DEPLOY_PAYMENT_MOP_UP_JOB',
    '09_DEPLOY_FTP'
]

if len(sys.argv) < 2:
    sys.exit('Please provide a tag')

if len(sys.argv) < 3:
    sys.exit('Please provide an environment DEV or TST')

TAG = sys.argv[1]
ENV = sys.argv[2]

j = Jenkins(JENKINS_URL, auth=(JENKINS_USERNAME, JENKINS_PASSWORD))

def execute_job(job_name):
    full_project_name = ENV + '/' + job_name
    print(f'Building {full_project_name}')
    item = j.build_job(full_project_name)

    while not item.get_build():
        time.sleep(1)

    build = item.get_build()
    while not build.get_pending_input():
        time.sleep(1)
    print(f'Deploying tag {TAG} for {full_project_name}')
    build.get_pending_input().submit(input=TAG)

for job in JOB_NAMES:
    execute_job(job)