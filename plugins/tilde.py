from __future__ import print_function
from __future__ import unicode_literals

from rtmbot.core import Plugin


class TildePlugin(Plugin):

    def _should_process(self, text):
        return text.startswith('tilde') or text.startswith('@tilde')

    def _strip_prefix(self, text):
        return text.split('tilde')[1]

    def process_message(self, data):
        print(data)
        if self._should_process(data['text']):
            text = u"~ {} ~".format(self._strip_prefix(data['text']))
            self.outputs.append([data['channel'], text])
