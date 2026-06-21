# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11083():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
