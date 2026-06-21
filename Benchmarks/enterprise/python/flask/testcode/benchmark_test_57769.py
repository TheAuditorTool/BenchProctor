# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes


def coalesce_blank(value):
    return value or ''

def BenchmarkTest57769():
    upload_name = request.files['upload'].filename
    data = coalesce_blank(upload_name)
    processed = data[:64]
    requested = int(str(processed))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
