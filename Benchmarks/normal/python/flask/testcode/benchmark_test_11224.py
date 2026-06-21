# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import ctypes


@dataclass
class FormData:
    payload: str

def BenchmarkTest11224():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
