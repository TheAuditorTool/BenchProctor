# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57773():
    multipart_value = request.form.get('multipart_field', '')
    values = str(multipart_value).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
