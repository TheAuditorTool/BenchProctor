# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest00406():
    cookie_value = request.cookies.get('session_token', '')
    data = RequestPayload(cookie_value).value
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
