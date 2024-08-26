import os
class Config:
    def __init__(self):
        self.ENV =""
        self.CUSTOMIZER_URL = ""

    def load(self):
        self.ENV = os.environ.get("ENV")