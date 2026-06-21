# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37414():
    multipart_value = request.form.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
