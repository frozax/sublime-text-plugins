import sublime_plugin

class FindInFilesNoSelection(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        sel = view.sel()
        selected_text = view.substr(sel[0])
        if selected_text == "":
            self.window.run_command("find_under_expand")
        self.window.run_command("show_panel", {"panel": "find_in_files"} )
