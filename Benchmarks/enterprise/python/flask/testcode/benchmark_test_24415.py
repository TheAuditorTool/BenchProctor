# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import runpy


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest24415():
    ua_value = request.headers.get('User-Agent', '')
    data = RequestPayload(ua_value).value
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
