# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest52755():
    upload_name = request.files['upload'].filename
    data = ensure_str(upload_name)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
