# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes


request_state: dict[str, str] = {}

def BenchmarkTest22355():
    field_value = request.form.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
