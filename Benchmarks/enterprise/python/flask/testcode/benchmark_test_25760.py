# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest25760():
    referer_value = request.headers.get('Referer', '')
    data = RequestPayload(referer_value).value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
