# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11202():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
