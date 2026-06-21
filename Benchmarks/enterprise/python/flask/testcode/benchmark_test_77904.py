# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import tempfile


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest77904():
    auth_header = request.headers.get('Authorization', '')
    data = RequestPayload(auth_header).value
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
