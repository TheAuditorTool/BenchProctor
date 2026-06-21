# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest02034():
    auth_header = request.headers.get('Authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
