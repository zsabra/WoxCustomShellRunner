# -*- coding: utf-8 -*-

from wox import Wox
from wox import WoxAPI
import os
import json
import subprocess
import webbrowser


class WSL(Wox):

    def query(self, query):
        results = []
        results.append({
            "Title": "$ " + query,
            "IcoPath": "icon/launcher.png",
            "JsonRPCAction": {
                "method": "executeCommand",
                "parameters": [query],
                "dontHideAfterAction": True
            }
        })
        return results

    def executeCommand(self, query):
        subprocess = subprocess.Popen(
            'wsl ' + query, shell=True, stdout=subprocess.PIPE)
        subprocess_return = subprocess.stdout.read()

        WoxAPI.show_msg(str(subprocess_return), "")
        f = open("log.txt", "w")
        f.write(str(subprocess_return) + "\n")
        f.close()

    def context_menu(self, data):
        results = []
        results.append({
            "Title": "Context menu entry",
            "SubTitle": "Data: {}".format(data),
            "IcoPath": "Images/app.ico"
        })
        return results


if __name__ == "__main__":
    WSL()
