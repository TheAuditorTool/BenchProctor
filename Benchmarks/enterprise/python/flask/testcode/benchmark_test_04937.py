# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04937():
    multipart_value = request.form.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
