# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest36883():
    upload_name = request.files['upload'].filename
    data = '%s' % (upload_name,)
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
