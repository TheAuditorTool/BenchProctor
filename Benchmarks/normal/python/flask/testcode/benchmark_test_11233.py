# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11233():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
