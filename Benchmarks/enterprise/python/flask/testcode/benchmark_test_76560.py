# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76560():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
