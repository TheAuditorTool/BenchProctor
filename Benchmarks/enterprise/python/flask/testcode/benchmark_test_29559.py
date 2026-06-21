# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes


def ensure_str(value):
    return str(value)

def BenchmarkTest29559():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
