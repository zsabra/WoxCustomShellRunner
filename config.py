import json
import pathlib
import os
import logging

class Config:
    def __init__(self, defaultConfig={}):
        self.config = defaultConfig
        self.plugin = {}
        self.loadConfig()

    def loadConfig(self):
        if not os.path.isfile("config.json"):
            self.saveConfig()

        with open("config.json") as json_data_file:
            self.config.update(json.load(json_data_file))

        with open("plugin.json") as json_data_file:
            self.plugin.update(json.load(json_data_file))

        logging.basicConfig(filename='.log', encoding='utf-8', level=self.get("logLevel"))

    def saveConfig(self):
        with open('config.json', 'w') as fp:
            json.dump(self.config, fp, sort_keys=True, indent=4)

    def getLocation(self):
        return pathlib.Path().absolute() + "config.json"

    def setConfig(self, key, value):
        self.config[key] = value
        self.saveConfig()

    def get(self, key):
        if self.config[key] is not None:
            return self.config[key]
        return self.plugin[key]
