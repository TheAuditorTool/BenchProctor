# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes


def BenchmarkTest71308():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % (forwarded_ip,)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
