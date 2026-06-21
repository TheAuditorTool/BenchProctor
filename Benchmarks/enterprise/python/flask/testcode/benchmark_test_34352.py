# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34352():
    multipart_value = request.form.get('multipart_field', '')
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(multipart_value)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
