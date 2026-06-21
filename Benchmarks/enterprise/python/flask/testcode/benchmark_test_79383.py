# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest79383():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
