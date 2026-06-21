# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest12065():
    origin_value = request.headers.get('Origin', '')
    data = RequestPayload(origin_value).value
    return Markup('<div>' + str(data) + '</div>')
