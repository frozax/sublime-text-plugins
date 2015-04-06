import os.path
from subprocess import Popen

import sublime_plugin


class CreateNewGcj(sublime_plugin.WindowCommand):

    def run(self):
        self.window.show_input_panel("Challenge name (e.g: B-Chall-Name", "", self.on_done, None, None)

    def on_done(self, chall_name):
        path = os.path.expanduser("~/challenges/gcj")
        p1 = Popen("cp -r %s/template %s/%s" % (path, path, chall_name), shell=True)
        self.window.run_command("set_layout", {"cells": [[0, 0, 1, 1]], "cols": [0.0, 1.0], "rows": [0.0, 1.0]})
        p1.wait()
        self.window.run_command("open_file", {"file": "%s/%s/code.py" % (path, chall_name)})
        self.window.run_command("create_pane", {"direction": "right", "give_focus": True})
        self.window.run_command("open_file", {"file": "%s/%s/in" % (path, chall_name)})
        self.window.run_command("create_pane", {"direction": "down", "give_focus": True})
        self.window.run_command("open_file", {"file": "%s/%s/out" % (path, chall_name)})
