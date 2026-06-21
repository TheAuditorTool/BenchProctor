# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest71799():
    upload_name = request.files['upload'].filename
    data = RequestPayload(upload_name).value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
