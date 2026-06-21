# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54680():
    upload_name = request.files['upload'].filename
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(upload_name)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
