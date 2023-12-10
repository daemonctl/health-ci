import configparser


class Config:
    config = None

    def __init__(self):
        self.bard_api_keys = None
        self.config = configparser.ConfigParser()
        self.config.read('./config.ini')

    def get_bard_api_key(self):
        bard_api_keys = self.config.get("TEST", "BARDAPIKEYS")
        return bard_api_keys