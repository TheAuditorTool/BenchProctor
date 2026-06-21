# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest75019():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    session['data'] = str(data)
    return jsonify({"result": "success"})
