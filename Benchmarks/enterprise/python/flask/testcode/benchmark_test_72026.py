# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes


def BenchmarkTest72026():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
