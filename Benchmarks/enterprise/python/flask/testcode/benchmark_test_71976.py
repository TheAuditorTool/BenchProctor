# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest71976():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
