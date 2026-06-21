# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68341():
    ua_value = request.headers.get('User-Agent', '')
    if ua_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = ua_value
    with open('/var/app/data/' + str(processed), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
