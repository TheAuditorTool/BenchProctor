# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes


def to_text(value):
    return str(value).strip()

def BenchmarkTest46472():
    cookie_value = request.cookies.get('session_token', '')
    data = to_text(cookie_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
