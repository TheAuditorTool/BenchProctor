# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00564():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    eval(str(data))
    return jsonify({"result": "success"})
