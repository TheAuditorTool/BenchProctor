# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11514():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    eval(str(data))
    return jsonify({"result": "success"})
