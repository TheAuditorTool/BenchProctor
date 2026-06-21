# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest04031():
    header_value = request.headers.get('X-Custom-Header', '')
    data = RequestPayload(header_value).value
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
