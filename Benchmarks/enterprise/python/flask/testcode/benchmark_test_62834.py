# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62834():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    int(str(data))
    return jsonify({"result": "success"})
