# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest20833():
    user_id = request.args.get('id', '')
    data = RequestPayload(user_id).value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
