# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import ctypes


def BenchmarkTest18992():
    referer_value = request.headers.get('Referer', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
