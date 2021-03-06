import sys

if sys.version_info < (3,):
    from lib.thread_progress import ThreadProgress
    from lib.show_error import *
    from lib.command_setup import command_setup
    from lib.printer import p
else:
    from .lib.thread_progress import ThreadProgress
    from .lib.show_error import *
    from .lib.command_setup import command_setup
    from .lib.printer import p


class BaseCommand():
    def run(self, modifier='', edit=None):
        setup_was_successful = command_setup(self)

        if not setup_was_successful:
            p('Setup was not successful')

        if modifier:
            self.view.modifier = modifier
        else:
            self.view.modifier = None

        if edit:
            self.view.edit = edit

        return setup_was_successful

    def init_thread(self, Thread, progress_message):
        thread = Thread(self)
        thread.start()

        ThreadProgress(thread, progress_message, '')
