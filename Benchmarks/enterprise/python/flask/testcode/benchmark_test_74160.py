# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74160():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
