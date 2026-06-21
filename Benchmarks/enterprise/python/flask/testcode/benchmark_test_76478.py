# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest76478():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = RequestPayload(dotenv_value).value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
