# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41288():
    upload_name = request.files['upload'].filename
    data, _sep, _rest = str(upload_name).partition('\x00')
    eval(str(data))
    return jsonify({"result": "success"})
