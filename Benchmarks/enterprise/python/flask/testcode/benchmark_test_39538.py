# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39538():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
