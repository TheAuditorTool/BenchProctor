# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15522():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
