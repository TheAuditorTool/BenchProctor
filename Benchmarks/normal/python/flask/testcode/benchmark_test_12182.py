# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest12182():
    referer_value = request.headers.get('Referer', '')
    data = RequestPayload(referer_value).value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
