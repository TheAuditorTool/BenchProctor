# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06544():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
