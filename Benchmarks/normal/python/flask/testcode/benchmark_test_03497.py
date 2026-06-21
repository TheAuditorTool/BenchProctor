# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest03497():
    upload_name = request.files['upload'].filename
    data = RequestPayload(upload_name).value
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
