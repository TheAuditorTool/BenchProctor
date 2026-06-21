# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47490():
    upload_name = request.files['upload'].filename
    data = f'{upload_name}'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
