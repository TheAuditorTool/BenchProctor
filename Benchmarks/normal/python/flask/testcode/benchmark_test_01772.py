# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01772():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    exec(str(data))
    return jsonify({"result": "success"})
