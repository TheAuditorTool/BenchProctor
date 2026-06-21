# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56994():
    upload_name = request.files['upload'].filename
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(upload_name)}
