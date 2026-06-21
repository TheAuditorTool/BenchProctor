# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
import ctypes


def BenchmarkTest76362():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
