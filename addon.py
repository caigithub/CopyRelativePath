
import sublime, sublime_plugin
import os

class CopyRelativePathCommand(sublime_plugin.WindowCommand):
    def run(self, suggests=[]):
        if not self.window.active_view():
            return

        file_full_path = self.window.active_view().file_name()
        if not file_full_path:
            return

        for folder in self.window.folders():
            if folder in file_full_path:
                relative_path = file_full_path.replace(folder + "\\", '')
                relative_path =  relative_path.replace('\\\\','/')
                relative_path =  relative_path.replace('\\','/')

                sublime.set_clipboard(relative_path)
                return

        return


class CopyFileNameCommand(sublime_plugin.WindowCommand):
    def run(self, suggests=[]):
        if not self.window.active_view():
            return

        file_full_path = self.window.active_view().file_name()
        if not file_full_path:
            return

        sublime.set_clipboard(os.path.basename(file_full_path))

        return