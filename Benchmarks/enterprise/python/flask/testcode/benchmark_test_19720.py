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

def BenchmarkTest19720():
    cookie_value = request.cookies.get('session_token', '')
    data = RequestPayload(cookie_value).value
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
