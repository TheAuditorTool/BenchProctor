# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest02105():
    auth_header = request.headers.get('Authorization', '')
    data = default_blank(auth_header)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
