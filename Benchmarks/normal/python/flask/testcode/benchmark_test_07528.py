# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07528():
    auth_header = request.headers.get('Authorization', '')
    data = '{}'.format(auth_header)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
