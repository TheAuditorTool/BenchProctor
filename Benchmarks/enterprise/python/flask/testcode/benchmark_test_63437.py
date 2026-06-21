# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest63437():
    multipart_value = request.form.get('multipart_field', '')
    data = RequestPayload(multipart_value).value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
