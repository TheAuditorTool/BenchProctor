# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest45916():
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
