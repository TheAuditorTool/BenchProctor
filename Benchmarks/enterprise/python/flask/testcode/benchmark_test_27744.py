# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest27744():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    session['data'] = str(data)
    return jsonify({"result": "success"})
