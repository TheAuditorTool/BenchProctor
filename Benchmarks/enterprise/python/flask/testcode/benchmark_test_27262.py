# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes


def relay_value(value):
    return value

def BenchmarkTest27262():
    host_value = request.headers.get('Host', '')
    data = relay_value(host_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
