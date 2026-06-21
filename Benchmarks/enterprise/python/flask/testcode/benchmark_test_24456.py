# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest24456():
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return jsonify({"result": "success"})
