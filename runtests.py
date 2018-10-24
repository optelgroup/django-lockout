import django
from django.conf import settings
from django.core.management import call_command


def runtests():
    if not settings.configured:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'foo'
            }
        }

        INSTALLED_APPS = (
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'lockout'
        )

        settings.configure(
            DATABASES=DATABASES,
            INSTALLED_APPS=INSTALLED_APPS,
            ROOT_URLCONF=''
        )

    django.setup()
    call_command('test', 'lockout', interactive=False, failfast=False, verbosity=2)


if __name__ == '__main__':
    runtests()
