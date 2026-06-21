# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest80493():
    ua_value = request.headers.get('User-Agent', '')
    data = RequestPayload(ua_value).value
    return Markup('<div>' + str(data) + '</div>')
