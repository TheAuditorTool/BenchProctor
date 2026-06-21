# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest37195():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
