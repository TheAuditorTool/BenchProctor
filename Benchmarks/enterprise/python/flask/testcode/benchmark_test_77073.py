# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest77073():
    upload_name = request.files['upload'].filename
    data = ensure_str(upload_name)
    session['user'] = str(data)
    return jsonify({"result": "success"})
