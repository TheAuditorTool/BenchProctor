# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest32688():
    host_value = request.headers.get('Host', '')
    data = RequestPayload(host_value).value
    return Markup('<div>' + str(data) + '</div>')
