# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest03306():
    upload_name = request.files['upload'].filename
    data = RequestPayload(upload_name).value
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
