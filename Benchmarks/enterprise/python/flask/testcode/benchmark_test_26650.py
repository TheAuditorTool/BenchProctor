# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26650():
    upload_name = request.files['upload'].filename
    data = f'{upload_name}'
    eval(str(data))
    return jsonify({"result": "success"})
