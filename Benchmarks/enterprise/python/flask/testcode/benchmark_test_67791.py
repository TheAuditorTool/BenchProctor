# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import runpy


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest67791():
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
