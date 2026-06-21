# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest16315():
    header_value = request.headers.get('X-Custom-Header', '')
    data = RequestPayload(header_value).value
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
