# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest69170():
    origin_value = request.headers.get('Origin', '')
    data = RequestPayload(origin_value).value
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
