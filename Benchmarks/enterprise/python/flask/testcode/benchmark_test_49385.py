# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49385():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
