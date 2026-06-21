# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest68389():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = RequestPayload(forwarded_ip).value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
