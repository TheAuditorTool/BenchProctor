# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00768():
    raw_body = request.get_data(as_text=True)
    data = '%s' % str(raw_body)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
