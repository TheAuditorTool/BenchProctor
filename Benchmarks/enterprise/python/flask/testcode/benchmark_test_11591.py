# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest11591():
    upload_name = request.files['upload'].filename
    data = RequestPayload(upload_name).value
    os.remove(str(data))
    return jsonify({"result": "success"})
