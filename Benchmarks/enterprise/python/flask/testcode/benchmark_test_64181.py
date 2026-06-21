# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64181():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
