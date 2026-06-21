# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10572():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
