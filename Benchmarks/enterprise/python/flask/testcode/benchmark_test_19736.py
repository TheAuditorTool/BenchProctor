# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes


def BenchmarkTest19736():
    ua_value = request.headers.get('User-Agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
