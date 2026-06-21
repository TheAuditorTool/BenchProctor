# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13804():
    xml_value = request.get_data(as_text=True)
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
