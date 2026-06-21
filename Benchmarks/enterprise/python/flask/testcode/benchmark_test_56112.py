# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56112():
    upload_name = request.files['upload'].filename
    data = '%s' % (upload_name,)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
