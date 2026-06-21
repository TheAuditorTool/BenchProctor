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

def BenchmarkTest12704():
    multipart_value = request.form.get('multipart_field', '')
    data = RequestPayload(multipart_value).value
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
