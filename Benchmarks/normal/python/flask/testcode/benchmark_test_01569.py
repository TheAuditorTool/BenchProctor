# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest01569():
    upload_name = request.files['upload'].filename
    ctx = RequestContext(upload_name)
    data = ctx.payload
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
