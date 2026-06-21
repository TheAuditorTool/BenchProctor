# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19240():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return jsonify({"result": "success"})
