# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest46313():
    auth_header = request.headers.get('Authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    os.remove(str(data))
    return jsonify({"result": "success"})
