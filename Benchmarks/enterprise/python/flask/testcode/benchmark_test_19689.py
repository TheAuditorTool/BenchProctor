# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes


def BenchmarkTest19689():
    upload_name = request.files['upload'].filename
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
