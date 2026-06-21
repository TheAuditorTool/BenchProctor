# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13657():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
