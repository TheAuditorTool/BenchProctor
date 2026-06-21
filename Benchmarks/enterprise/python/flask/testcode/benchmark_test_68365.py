# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68365():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value}'
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
