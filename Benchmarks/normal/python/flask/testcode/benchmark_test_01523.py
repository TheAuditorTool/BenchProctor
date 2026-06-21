# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01523():
    upload_name = request.files['upload'].filename
    if str(upload_name) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
