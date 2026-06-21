# SPDX-License-Identifier: Apache-2.0
from flask import request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest33519():
    raw_body = request.get_data(as_text=True)
    data = RequestPayload(raw_body).value
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
