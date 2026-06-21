# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes


def BenchmarkTest77439():
    multipart_value = request.form.get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
