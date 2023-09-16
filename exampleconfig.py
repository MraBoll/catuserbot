from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 16456909
    API_HASH = "5b668492cc9e6db053af33063450bcd5"
    # the name to display in your alive message
    ALIVE_NAME = "Viru3"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://gepgwedw:zK4DYyC29u8pkClIZzCZEjJv5nOAtELD@trumpet.db.elephantsql.com/gepgwedw"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BFtsBLEBux8j2UV9pkEv41tH5-sWa2YC_i1IjzqTIn0_J2kY9nJKCaSmTH8I81A3yEQnkhcaqBEjjnKMZnOvjf4qKvbVvGO53iDJLEnpGAL2V0xKM4sKneaUpmskpXCRbc5xtCE67OQ29b-EWVvvUPNUXenPVgafYyoYx-eJ2Xf-bZf23qRNjzWgLiGmIel2svVuOOD76y7fUz10UtpDhTgF_f9xuHZVKc_a7uOi1iHUZ6xQphl2pcecBWjj1InOYG8qRLs1FInyo-dMKFNjS2qgBxX3QjZ7zgotx6r5RHO5WBjjRDISRpAA_-BcJwBCCt2dF-BqZ5xMniUzD-j69MWZa5WWL5Y="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6665869643:AAEX4PC-scT74Mq3DjKjntaA_dfdz9JxOrc"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001693039993
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
