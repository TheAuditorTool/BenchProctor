# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38210():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
