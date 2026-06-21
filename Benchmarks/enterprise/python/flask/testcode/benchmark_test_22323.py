# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22323():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    eval(str(data))
    return jsonify({"result": "success"})
