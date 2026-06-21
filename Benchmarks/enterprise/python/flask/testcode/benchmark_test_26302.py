# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest26302():
    upload_name = request.files['upload'].filename
    data = f'{upload_name}'
    json.loads(data)
    return jsonify({"result": "success"})
