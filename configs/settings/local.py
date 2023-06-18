
import os

from .base import *


######################################################################
#                                                                    #
# python manage.py runserver --settings=configs.settings.local       #
#                                                                    #
######################################################################


JIRA_API_KEY = os.getenv('ATLASSIAN_API_TOKEN')
