# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes


def BenchmarkTest38119():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
