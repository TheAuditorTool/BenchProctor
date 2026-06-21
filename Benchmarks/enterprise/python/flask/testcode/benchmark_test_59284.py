# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59284():
    upload_name = request.files['upload'].filename
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(upload_name)}
