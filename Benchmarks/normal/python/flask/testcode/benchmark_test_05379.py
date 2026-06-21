# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import runpy


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest05379():
    auth_header = request.headers.get('Authorization', '')
    data = RequestPayload(auth_header).value
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
