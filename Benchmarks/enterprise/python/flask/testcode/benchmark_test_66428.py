# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest66428():
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
