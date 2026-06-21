# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest35713():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    session['data'] = str(data)
    return jsonify({"result": "success"})
