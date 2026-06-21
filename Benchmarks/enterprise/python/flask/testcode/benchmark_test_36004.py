# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest36004():
    upload_name = request.files['upload'].filename
    data, _sep, _rest = str(upload_name).partition('\x00')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
