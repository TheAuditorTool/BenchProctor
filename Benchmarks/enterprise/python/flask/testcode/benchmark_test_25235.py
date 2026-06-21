# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest25235():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    session['data'] = str(data)
    return jsonify({"result": "success"})
