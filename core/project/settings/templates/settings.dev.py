from core.project.settings.logging import LOGGING

DEBUG = True
SECRET_KEY = 'YOUR SECRET KEY'

LOGGING['formatters']['colored'] = {   # type:ignore
    '()': 'colorlog.ColoredFormatter',
    'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s',
}
LOGGING['loggers']['core']['level'] = 'DEBUG'  # type:ignore
LOGGING['handlers']['console']['level'] = 'DEBUG'  # type:ignore
LOGGING['handlers']['console']['formatter'] = 'colored'  # type:ignore
