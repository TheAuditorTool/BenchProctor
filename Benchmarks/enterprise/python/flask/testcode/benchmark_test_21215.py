# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21215():
    upload_name = request.files['upload'].filename
    data = '{}'.format(upload_name)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
