# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30557():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    exec(str(data))
    return jsonify({"result": "success"})
