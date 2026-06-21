# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60990():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    eval(str(data))
    return jsonify({"result": "success"})
