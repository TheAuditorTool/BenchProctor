# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import ctypes


@dataclass
class FormData:
    payload: str

def BenchmarkTest42458():
    host_value = request.headers.get('Host', '')
    data = FormData(payload=host_value).payload
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
