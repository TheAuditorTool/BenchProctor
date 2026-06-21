# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35202():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '%s' % (json_value,)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
