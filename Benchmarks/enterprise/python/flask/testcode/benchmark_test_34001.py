# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest34001():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = RequestPayload(json_value).value
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
