# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest57088():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    session['data'] = str(data)
    return jsonify({"result": "success"})
