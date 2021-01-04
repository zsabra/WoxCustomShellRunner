# -*- coding: utf-8 -*-

from wox import Wox, WoxAPI
import os
import json
import subprocess
import webbrowser
from config import Config
from log import info, exceptionHandler
from shlex import split, quote, join
import sys
import logging


sys.excepthook = exceptionHandler

config = Config({
    "logLevel": 10,
    "launchers": [{
        "showName": False,
        "command": ['wsl.exe'],
        "suffix": ["&&", "sleep", "2"],
        "name": "bash",
        "icon": "Images\\terminal.png"
    }, {
        "showName": False,
        "command": ['cmd.exe', '/c'],
        "suffix": ["&", "timeout", "4"],
        "name": "cmd",
        "icon": "Images\\terminal.png"
    }, {
        "showName": False,
        "command": ['powershell.exe'],
        "suffix": ["-and", "Start-Sleep", "-s", "15"],
        "name": "ps",
        "icon": "Images\\terminal.png"
    }],
})

defaultIcon = "Images\\terminal.png"


class ShellLauncher(Wox):

    def query(self, query):
        launchers = config.get("launchers")
        results = map(lambda launcher: self.formatResult(
            launcher, query), launchers)
        return list(results)

    def formatResult(self, launcher, query):
        command = launcher.get("command") if launcher.get(
            "command") is not None else []
        suffix = launcher.get("suffix") if launcher.get(
            "suffix") is not None else []
        result = {
            "Title": "Run '" + query + "'",
            "Subtitle": "Using " + launcher.get("name") if launcher.get("showName") == True else " ".join(self.parseCommand(command, query, suffix)),
            "IcoPath": launcher.get("icon") if launcher.get("icon") is not None else defaultIcon,
            "JsonRPCAction": {
                "method": "executeCommand",
                "parameters": [json.dumps(command), query, json.dumps(suffix)],
                "dontHideAfterAction": False
            }
        }
        return result

    def executeCommand(self, prefix, query, suffix):
        prefix = json.loads(prefix)
        suffix = json.loads(suffix)
        command = self.parseCommand(prefix, query, suffix)
        try:
            subprocess.run(command)
        except:
            info(["Caught error"])

    def parseCommand(self, prefix, query, suffix):
        return prefix + split(query) + suffix

    def reloadConfig(self):
        config.loadConfig()

    def context_menu(self, data):
        results = []
        results.append({
            "Title": "Reload config",
            "IcoPath": defaultIcon,
            "JsonRPCAction": {
                "method": "reloadConfig",
                "parameters": [],
                "dontHideAfterAction": False
            }
        })
        return results


if __name__ == "__main__":
    ShellLauncher()
