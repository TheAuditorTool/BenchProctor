# SPDX-License-Identifier: Apache-2.0
from flask import request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest01972():
    user_id = request.args.get('id', '')
    data = RequestPayload(user_id).value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
