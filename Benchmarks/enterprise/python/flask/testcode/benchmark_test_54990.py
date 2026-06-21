# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54990():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
