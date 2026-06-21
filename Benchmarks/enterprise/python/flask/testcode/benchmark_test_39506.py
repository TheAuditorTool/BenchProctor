# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest39506():
    referer_value = request.headers.get('Referer', '')
    data = handle(referer_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
