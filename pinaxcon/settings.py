import os
import dj_database_url

CONFERENCE_YEAR = '2018'
URL_PREFIX = "/%s" % CONFERENCE_YEAR
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = PACKAGE_ROOT
ARCHIVE_ROOT = os.path.join(PROJECT_ROOT, 'archive')

DEBUG = bool(int(os.environ.get("DEBUG", "1")))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(PROJECT_ROOT, "dev.db"),
    }
}

UNPREPEND_WWW = bool(int(os.environ.get("DJANGO_UNPREPEND_WWW", "0")))

# HEROKU: Update database configuration with $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS = [".pyohio.org", ".localhost", ".herokuapp.com"]
CANONICAL_HOST = os.environ.get("DJANGO_CANONICAL_HOST", None)

# If DEFAULT_FROM_EMAIL is not set, email will most likely break in prod.
from_email = os.environ.get("DJANGO_DEFAULT_FROM_EMAIL", None)
if from_email is not None:
    DEFAULT_FROM_EMAIL = from_email
    SERVER_EMAIL = DEFAULT_FROM_EMAIL

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = os.environ.get("TZ", "America/Los_Angeles")


# Set the email address that will receive errors.
admin_email = os.environ.get("DJANGO_ADMIN_EMAIL", None)
if admin_email is not None:
    ADMINS = [("Webmaster", admin_email)]


# Use SSLRedirectMiddleware
SSL_ON = os.environ.get("DJANGO_SSL_ON", True)
SSL_ALWAYS = os.environ.get("DJANGO_SSL_ALWAYS", False)

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = int(os.environ.get("SITE_ID", 1))

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "%s/site_media/media/" % URL_PREFIX

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = COMPRESS_URL = '%s/static/' % URL_PREFIX

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]


# Amazon S3 setup
DEFAULT_FILE_STORAGE = os.environ.get("DJANGO_DEFAULT_FILE_STORAGE", 'django.core.files.storage.FileSystemStorage') # noqa
THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE
AWS_ACCESS_KEY_ID = os.environ.get("DJANGO_AWS_ACCESS_KEY_ID", None)
AWS_SECRET_ACCESS_KEY = os.environ.get("DJANGO_AWS_SECRET_ACCESS_KEY", None)
AWS_STORAGE_BUCKET_NAME = os.environ.get("DJANGO_AWS_STORAGE_BUCKET_NAME", None)
STATICFILES_STORAGE = COMPRESS_STORAGE =  os.environ.get("DJANGO_STATICFILES_STORAGE", None)
AWS_S3_REGION_NAME = os.environ.get("DJANGO_S3_REGION", None)
AWS_QUERYSTRING_AUTH = False

if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY:
    # Re-assign static URLs to point to the s3 bucket
    STATIC_URL = COMPRESS_URL = 'https://s3.{0}.amazonaws.com/{1}/'.format(
        os.environ.get("DJANGO_S3_REGION", "us-east-2"),
        AWS_STORAGE_BUCKET_NAME)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
if DEBUG and not SECRET_KEY:
    SECRET_KEY = "711d8b059214f9a496ab5e8df8fc6db2bfd0da1863a8cb6ae01be9f4da69434e"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PACKAGE_ROOT, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": DEBUG,
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
                "account.context_processors.account",
                "pinax_theme_bootstrap.context_processors.theme",
                "symposion.reviews.context_processors.reviews",
                "sekizai.context_processors.sekizai",
                "pinaxcon.context_processors.site_settings",
            ],
        },
    },
]

TEMPLATE_DEBUG = False

MIDDLEWARE_CLASSES = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "reversion.middleware.RevisionMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "ssl_redirect.middleware.SSLRedirectMiddleware",
    "pinaxcon.middleware.CanonicalHostMiddleware",
    "pinaxcon.middleware.UnprependWWWMiddleware",
    "pinaxcon.monkey_patch.MonkeyPatchMiddleware",
    "rollbar.contrib.django.middleware.RollbarNotifierMiddleware",
]

ROOT_URLCONF = "pinaxcon.urls"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "pinaxcon.wsgi.application"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",

    # theme
    "bootstrapform",
    "pinax_theme_bootstrap",

    # external
    "account",
    "easy_thumbnails",
    "taggit",
    "reversion",
    "metron",
    "sitetree",
    "pinax.boxes",
    "pinax.eventlog",
    "pinax.pages",
    "markdown_deux",

    # symposion
    "symposion",
    "symposion.conference",
    "symposion.proposals",
    "symposion.reviews",
    "symposion.schedule",
    "symposion.speakers",
    "symposion.sponsorship",
    "symposion.teams",

    # Registrasion
    "registrasion",
    "symposion_templates",

    # Registrasion-stipe
    "pinax.stripe",
    "django_countries",
    "registripe",

    #admin - required by registrasion ??
    "nested_admin",

    # project
    "pinaxcon",
    "pinaxcon.proposals",
    "pinaxcon.registrasion",

    #testing
    "django_nose",

    # wiki
    'django.contrib.humanize',
    'django_nyt',
    'mptt',
    'sekizai',
    #'sorl.thumbnail',
    'wiki',
    'wiki.plugins.attachments',
    'wiki.plugins.notifications',
    #'wiki.plugins.images',
    'wiki.plugins.macros',

    # stylesheets and js
    'compressor',

    'email_log',
    'storages',
]

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    }
}

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

# Heroku: Get email configuration from environment variables.

EMAIL_BACKEND = "email_log.backends.EmailBackend"
EMAIL_LOG_BACKEND = os.environ.get("DJANGO_EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend")  # noqa
EMAIL_HOST = os.environ.get("DJANGO_EMAIL_HOST", "")
EMAIL_PORT = int(os.environ.get("DJANGO_EMAIL_PORT", 25))
EMAIL_HOST_USER = os.environ.get("DJANGO_EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("DJANGO_EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = bool(int(os.environ.get("DJANGO_EMAIL_USE_TLS", "0")))
EMAIL_USE_SSL = bool(int(os.environ.get("DJANGO_EMAIL_USE_SSL", "0")))

ACCOUNT_LOGIN_URL = "dashboard_login"
LOGIN_URL = "dashboard_login"

# We need to explicitly switch on signups.
ACCOUNT_OPEN_SIGNUP = bool(int(os.environ.get("DJANGO_ACCOUNT_OPEN_SIGNUP", "0")))
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False if DEBUG else True
ACCOUNT_LOGIN_REDIRECT_URL = "dashboard"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
ACCOUNT_USE_AUTH_AUTHENTICATE = True
ACCOUNT_HOOKSET =  "pinaxcon.account_hooks.BetterAccountHookSet"

AUTHENTICATION_BACKENDS = [
    "symposion.teams.backends.TeamPermissionsBackend",
    "account.auth_backends.UsernameAuthenticationBackend",
]

CONFERENCE_ID = 1
PROPOSAL_FORMS = {
    "talk": "pinaxcon.proposals.forms.TalkProposalForm",
    "tutorial": "pinaxcon.proposals.forms.TutorialProposalForm",
}
PINAX_PAGES_HOOKSET = "pinaxcon.hooks.PinaxPagesHookSet"
PINAX_BOXES_HOOKSET = "pinaxcon.hooks.PinaxBoxesHookSet"

PINAX_STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY", "your test public key")
PINAX_STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "your test secret key")
TUOKCEHC_BASE_URL = os.environ.get("TUOKCEHC_BASE_URL", None)
PINAX_STRIPE_SEND_EMAIL_RECEIPTS = False

SYMPOSION_SPEAKER_MODEL = "pinaxcon.proposals.models.ConferenceSpeaker"
SYMPOSION_SPEAKER_FORM = "pinaxcon.proposals.forms.ConferenceSpeakerForm"

# Registrasion Attendee profile model
ATTENDEE_PROFILE_MODEL = "pinaxcon.registrasion.models.AttendeeProfile"
# Registrasion attendee profile form -- must act on ATTENDEE_PROFILE_FORM
# You only need to provide this if you're customising the form from the default
# ATTENDEE_PROFILE_FORM = "pinaxcon.registrasion.forms.ProfileForm"

# Ticket product category -- used to identify which products must be available
# in order to register.
TICKET_PRODUCT_CATEGORY = 1


INVOICE_CURRENCY = "USD"

WIKI_ACCOUNT_HANDLING = False
WIKI_ACCOUNT_SIGNUP_ALLOWED = False

WIKI_ANONYMOUS_WRITE = False
WIKI_ANONYMOUS_UPLOAD = False


# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'


# Tell nose to measure coverage on the 'foo' and 'bar' apps
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=registrasion.controllers,registrasion.models',
]

MARKDOWN_DEUX_STYLES = {
    "default": {
        "safe_mode": False,
        "extras": {
            "tables": 1,
        }
    },
}

# Use Django-lockdown to password-protect staging / preview sites
LOCKDOWN_SITE = os.environ.get('LOCKDOWN_SITE', False)
if LOCKDOWN_SITE:
    INSTALLED_APPS += ('lockdown',)
    MIDDLEWARE_CLASSES += ('lockdown.middleware.LockdownMiddleware',)
    LOCKDOWN_PASSWORDS = (os.environ['LOCKDOWN_PASSWORD'],)
    LOCKDOWN_LOGOUT_KEY = 'logmeout'

# Rollbar monitoring and alerts configuration
ROLLBAR = {
    'access_token': os.environ.get('ROLLBAR_ACCESS_TOKEN'),
    'environment': 'development' if DEBUG else 'production',
    'branch': 'master',
    'root': PROJECT_ROOT,
}
