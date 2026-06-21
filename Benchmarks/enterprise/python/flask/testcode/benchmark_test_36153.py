# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest36153():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
