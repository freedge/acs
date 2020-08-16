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
from ansible.errors import AnsibleConnectionFailure
from ansible.module_utils._text import to_text


class TerminalModule(TerminalBase):
    terminal_stdout_re = [
        re.compile(br".*switch>"),
        re.compile(br"--:.*->")
    ]

    terminal_stderr_re = [
        re.compile(br"[\r\n]Error: .*[\r\n]+"),
        re.compile(br"[\r\n](MINOR|MAJOR|CRITICAL): .*[\r\n]+")
    ]

    def __init__(self, *args, **kwargs):
        super(TerminalModule, self).__init__(*args, **kwargs)

    def warning(self, msg):
        self._connection.queue_message('warning', msg)
