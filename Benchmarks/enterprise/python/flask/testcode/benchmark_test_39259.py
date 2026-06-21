# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39259():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('/var/app/data/' + str(processed), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
