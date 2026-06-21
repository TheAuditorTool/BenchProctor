# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes


def to_text(value):
    return str(value).strip()

def BenchmarkTest08876():
    header_value = request.headers.get('X-Custom-Header', '')
    data = to_text(header_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
