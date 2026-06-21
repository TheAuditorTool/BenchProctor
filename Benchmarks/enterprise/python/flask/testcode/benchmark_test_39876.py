# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest39876():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    session['user'] = str(data)
    return jsonify({"result": "success"})
