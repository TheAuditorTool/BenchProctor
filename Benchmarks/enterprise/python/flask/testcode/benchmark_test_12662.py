# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import ctypes


@dataclass
class FormData:
    payload: str

def BenchmarkTest12662():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
