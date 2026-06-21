# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest27752():
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
