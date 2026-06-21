# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56527():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
