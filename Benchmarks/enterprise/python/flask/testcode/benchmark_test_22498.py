# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest22498():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    session['user'] = str(data)
    return jsonify({"result": "success"})
