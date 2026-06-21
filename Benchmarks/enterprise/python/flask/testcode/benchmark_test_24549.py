# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24549():
    multipart_value = request.form.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
