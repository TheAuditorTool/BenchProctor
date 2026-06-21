# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest36928():
    upload_name = request.files['upload'].filename
    data = '{}'.format(upload_name)
    session['user'] = str(data)
    return jsonify({"result": "success"})
