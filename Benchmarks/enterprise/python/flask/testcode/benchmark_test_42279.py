# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest42279(path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
