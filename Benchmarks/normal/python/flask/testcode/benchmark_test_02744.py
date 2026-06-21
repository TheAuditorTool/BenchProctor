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

def BenchmarkTest02744():
    raw_body = request.get_data(as_text=True)
    data = RequestPayload(raw_body).value
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
