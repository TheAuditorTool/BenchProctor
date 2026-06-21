# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27473():
    upload_name = request.files['upload'].filename
    data = '{}'.format(upload_name)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
