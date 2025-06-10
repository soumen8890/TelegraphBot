import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7735245680:AAGA6un50i9FPtXHX-AcitLvqsvHBPIMDp4")

    APP_ID = int(os.environ.get("APP_ID", 20919625))

    API_HASH = os.environ.get("API_HASH", "40168846bf06f4ff443f0f7a4182bf8d")
