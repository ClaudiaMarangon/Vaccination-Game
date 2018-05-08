import os
from os import environ

import dj_database_url

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True

ADMIN_USERNAME = 'admin'

# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# don't share this with anybody.
SECRET_KEY = 'uv!rze_yo(%=36zz&)ei0m2j(!tecq&^_qpjc#+8i47c$9m)f0'

DATABASES = {
    'default': dj_database_url.config(
        # Rather than hardcoding the DB parameters here,
        # it's recommended to set the DATABASE_URL environment variable.
        # This will allow you to use SQLite locally, and postgres/mysql
        # on the server
        # Examples:
        # export DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
        # export DATABASE_URL=mysql://USER:PASSWORD@HOST:PORT/NAME

        # fall back to SQLite if the DATABASE_URL env var is missing
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# If you are launching a study and want visitors to only be able to
# play your app if you provided them with a start link, set the
# environment variable OTREE_AUTH_LEVEL to STUDY.
# If you would like to put your site online in public demo mode where
# anybody can play a demo version of your game, set OTREE_AUTH_LEVEL
# to DEMO. This will allow people to play in demo mode, but not access
# the full admin interface.

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True
POINTS_DECIMAL_PLACES = 0
POINTS_CUSTOM_NAME = ''


# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_HTML = """
oTree games
"""

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24,  # 7 days
    # 'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    # to use qualification requirements, you need to uncomment the 'qualification' import
    # at the top of this file.
    'qualification_requirements': [],
}

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.000,
    'participation_fee': 0.00,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}


SESSION_CONFIGS = [
    {
        'name': 'vg_neutralword',
        'display_name': "Vaccination Game - Neutral Wording 2 Players",
        'num_demo_participants': 2,
        'app_sequence': [
            'vg_naturalword',
        ],
    },

    {
        'name': 'vg_neutralword_3',
        'display_name': "Vaccination Game - Neutral Wording 3 Players",
        'num_demo_participants': 3,
        'app_sequence': [
            'vg_naturalword_3',
        ],
    },

    {
        'name': 'vg_vaccineword',
        'display_name': "Vaccination Game - Vaccination Wording",
        'num_demo_participants': 2,
        'app_sequence': [
            'vg_vaccineword',
        ],
    },

    {
        'name': 'vg_vaccineword_3',
        'display_name': "Vaccination Game - Vaccination Wording 3 Players",
        'num_demo_participants': 3,
        'app_sequence': [
            'vg_vaccineword_3',
        ],
    },

    {
        'name': 'vg_vaccinewordhigh',
        'display_name': "Vaccination Game - Vaccination Wording High Details, 3 Players",
        'num_demo_participants': 3,
        'app_sequence': [
            'vg_vaccinewordhigh',
        ],
    },

    {
        'name': 'vg_vaccinewordhigh_2',
        'display_name': "Vaccination Game - Vaccination Wording High Details, 2 Players",
        'num_demo_participants': 2,
        'app_sequence': [
            'vg_vaccinewordhigh_2',
        ],
    },

    {
        'name': 'vg_vaccinewordlow',
        'display_name': "Vaccination Game - Vaccination Wording Low Details",
        'num_demo_participants': 3,
        'app_sequence': [
            'vg_vaccinewordlow',
        ],
    },

    {
        'name': 'vg_vaccinewordlow_2',
        'display_name': "Vaccination Game - Vaccination Wording Low Details, 2 Players",
        'num_demo_participants': 2,
        'app_sequence': [
            'vg_vaccinewordlow_2',
        ],
    },

    {
        'name': 'survey',
        'display_name': "Survey",
        'num_demo_participants': 1,
        'app_sequence': [
            'survey',
        ],
    },
    {
        'name': 'session_one',
        'display_name': "Session 1 - 8th May",
        'num_demo_participants': 6,
        'app_sequence': [
            'vg_naturalword',
            'vg_naturalword_3',
            'survey',
        ],
    },

    {
        'name': 'session_two',
        'display_name': "Session 2 - 8th May",
        'num_demo_participants': 6,
        'app_sequence': [
            'vg_vaccinewordlow_2',
            'vg_vaccinewordlow',
            'survey',
        ],
    },
]

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
