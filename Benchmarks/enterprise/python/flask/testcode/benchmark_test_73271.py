# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73271():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
