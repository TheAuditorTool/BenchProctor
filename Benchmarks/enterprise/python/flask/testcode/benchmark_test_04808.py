# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
import ctypes


def BenchmarkTest04808():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
