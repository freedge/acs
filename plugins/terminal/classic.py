from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
---
author: Freedge
terminal: freedge.acs
short_description: CLI terminal support for ACS devices
"""

import re

from ansible.plugins.terminal import TerminalBase


class TerminalModule(TerminalBase):
    terminal_stdout_re = [
        re.compile(br".*switch>"),
        re.compile(br"--:.*->"),
        re.compile(br".admin@[^ ]* ...")
    ]

    terminal_stderr_re = [
        re.compile(br"[\r\n]Error: .*[\r\n]+"),
        re.compile(br"[\r\n](MINOR|MAJOR|CRITICAL): .*[\r\n]+")
    ]

    def __init__(self, *args, **kwargs):
        super(TerminalModule, self).__init__(*args, **kwargs)

    def warning(self, msg):
        self._connection.queue_message('warning', msg)

    # needed when connecting as admin
    def on_open_shell(self):
        self._exec_cli_command('cli')
