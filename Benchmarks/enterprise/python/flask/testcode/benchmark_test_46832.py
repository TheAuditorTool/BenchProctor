# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest46832():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    data = RequestPayload(query_array).value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
