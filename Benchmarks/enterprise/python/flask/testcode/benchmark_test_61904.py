# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest61904():
    cookie_value = request.cookies.get('session_token', '')
    data = RequestPayload(cookie_value).value
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
