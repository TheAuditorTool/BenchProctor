# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75944():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
