# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest10142():
    host_value = request.headers.get('Host', '')
    data = RequestPayload(host_value).value
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
