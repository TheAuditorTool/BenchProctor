# SPDX-License-Identifier: Apache-2.0
from flask import request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest45732():
    auth_header = request.headers.get('Authorization', '')
    data = RequestPayload(auth_header).value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
