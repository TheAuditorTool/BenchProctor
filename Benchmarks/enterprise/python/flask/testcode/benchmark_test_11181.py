# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11181():
    multipart_value = request.form.get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
