import uuid

import xbmc
from xbmcaddon import Addon

ADDON_ID = 'metadata.tvshows.thetvdb.v4.python'
ADDON = Addon()


class logger:
    log_message_prefix = '[{} ({})]: '.format(
        ADDON_ID, ADDON.getAddonInfo('version'))

    @staticmethod
    def log(message, level=xbmc.LOGDEBUG):
        message = logger.log_message_prefix + str(message)
        xbmc.log(message, level)

    @staticmethod
    def info(message):
        logger.log(message, xbmc.LOGINFO)

    @staticmethod
    def error(message):
        logger.log(message, xbmc.LOGERROR)

    @staticmethod
    def debug(message):
        logger.log(message, xbmc.LOGDEBUG)


def create_uuid():
    return str(uuid.uuid4())


def get_language(path_settings):
    language = path_settings.get('language')
    if language is None:
        language = ADDON.getSetting('language') or 'eng'
    return language

