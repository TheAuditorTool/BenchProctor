# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64680():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
