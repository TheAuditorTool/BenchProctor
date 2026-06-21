# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest07127():
    user_id = request.args.get('id', '')
    data = RequestPayload(user_id).value
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
