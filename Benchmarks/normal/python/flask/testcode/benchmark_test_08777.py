# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08777():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
