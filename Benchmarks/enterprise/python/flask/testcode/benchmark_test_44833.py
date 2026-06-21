# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest44833():
    auth_header = request.headers.get('Authorization', '')
    data = RequestPayload(auth_header).value
    return Markup('<div>' + str(data) + '</div>')
