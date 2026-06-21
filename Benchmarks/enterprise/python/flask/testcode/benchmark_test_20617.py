# SPDX-License-Identifier: Apache-2.0
from flask import request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest20617():
    referer_value = request.headers.get('Referer', '')
    data = RequestPayload(referer_value).value
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
