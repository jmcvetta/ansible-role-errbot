#===============================================================================
#
# Errbot Configuration
#
#-------------------------------------------------------------------------------
# {{ ansible_managed }}
#===============================================================================

import logging


{% if errbot_xmpp %}
BACKEND = 'XMPP'
{% elif errbot_hipchat %}
BACKEND = 'HipChat'
{% elif errbot_slack %}
BACKEND = 'Slack'
{% elif errbot_irc %}
BACKEND = 'IRC'
{% elif errbot_telegram %}
BACKEND = 'Telegram'
{% endif %}

BOT_DATA_DIR = '{{ errbot_bot_data_dir }}'
BOT_EXTRA_PLUGIN_DIR = {{ errbot_bot_extra_plugin_dir|quote }}
# BOT_EXTRA_BACKEND_DIR = '/opt/errbackends'
AUTOINSTALL_DEPS = {{ errbot_autoinstall_deps }}
BOT_LOG_FILE = '{{ errbot_log_file }}'
BOT_LOG_LEVEL = {{ errbot_bot_log_level }}
BOT_LOG_SENTRY = {{ errbot_bot_log_sentry }}
SENTRY_DSN = '{{ errbot_sentry_dsn }}'
SENTRY_LOGLEVEL = {{ errbot_sentry_loglevel }}
BOT_ASYNC = {{ errbot_bot_async }}

BOT_IDENTITY = {
{% if errbot_xmpp %}
    # XMPP mode
    'username': '{{ errbot_xmpp_username }}',  # The JID of the user you have created for the bot
    'password': '{{ errbot_xmpp_password }}',       # The corresponding password for this user
    {% if errbot_xmpp_server is defined %}
    'server': ('{{ errbot_xmpp_server }}', {{ errbot_xmpp_port }}), # server override
    {% endif %}
{% elif errbot_hipchat %}
    # HipChat mode
    'username' : '{{ errbot_hipchat_username }}',
    'password' : '{{ errbot_hipchat_password }}',
    {% if errbot_hipchat_token %}
    'token'    : '{{ errbot_hipchat_token }}',
    {% endif %}
    {% if errbot_hipchat_endpoint %}
    'endpoint' : '{{ errbot_hipchat_endpoint }}',
    {% endif %}
{% elif errbot_slack %}
    # Slack mode
    'token': '{{ errbot_slack_token }}',
{% elif errbot_telegram %}
    # Telegram mode
    'token': '{{ errbot_telegram_token }}',
    {% elif errbot_irc %}
    # IRC mode
    'nickname' : '{{ errbot_irc_nickname }}',
    'username' : '{{ errbot_irc_username }}',
    'server' : '{{ errbot_irc_server }}',
    {% if errbot_irc_password %}
    'password' : '{{ errbot_irc_password }}',
    {% endif %}
    {% if errbot_irc_port %}
    'port': {{ errbot_irc_port }},
    {% endif %}
    {% if errbot_irc_ssl %}
    'ssl': {{ errbot_irc_ssl }},
    {% endif %}
    {% if errbot_irc_nickserv_password %}
    'nickserv_password': {{ errbot_irc_nickserv_password }},
    {% endif %}
{% endif %}
}

BOT_ADMINS = {{ errbot_bot_admins }}
CHATROOM_PRESENCE = {{ errbot_chatroom_presence }}
CHATROOM_FN = '{{ errbot_chatroom_fn }}'
BOT_PREFIX = '{{ errbot_bot_prefix }}'
#BOT_PREFIX_OPTIONAL_ON_CHAT = False
#BOT_ALT_PREFIXES = ('Err',)
#BOT_ALT_PREFIX_SEPARATORS = (':', ',', ';')
#BOT_ALT_PREFIX_CASEINSENSITIVE = True
#ACCESS_CONTROLS_DEFAULT = {} # Allow everyone access by default
#ACCESS_CONTROLS = {'status': {'allowrooms': ('someroom@conference.localhost',)},
#                   'about': {'denyusers': ('baduser@localhost',), 'allowrooms': ('room1@conference.localhost', 'room2@conference.localhost')},
#                   'uptime': {'allowusers': BOT_ADMINS},
#                   'help': {'allowmuc': False},
#                  }
#HIDE_RESTRICTED_COMMANDS = False
#HIDE_RESTRICTED_ACCESS = False
DIVERT_TO_PRIVATE = ()
CHATROOM_RELAY = {}
REVERSE_CHATROOM_RELAY = {}
#MESSAGE_SIZE_LIMIT = 10000
#XMPP_CA_CERT_FILE = "/etc/ssl/certs/ca-certificates.crt"
#XMPP_FEATURE_MECHANISMS = {}
#XMPP_KEEPALIVE_INTERVAL = 300
#IRC_CHANNEL_RATE = 1  # Regular channel messages
#IRC_PRIVATE_RATE = 1  # Private messages
#IRC_RECONNECT_ON_KICK = 5  # Reconnect back to a channel after a kick (in seconds)
#IRC_RECONNECT_ON_DISCONNECT = 5  # Reconnect back to a channel after a disconenction (in seconds)
#GROUPCHAT_NICK_PREFIXED = False
# COMPACT_OUTPUT = True
# SUPPRESS_CMD_NOT_FOUND = False
