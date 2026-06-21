# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
import ctypes


def BenchmarkTest34243():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
