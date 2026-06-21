# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest70214():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
