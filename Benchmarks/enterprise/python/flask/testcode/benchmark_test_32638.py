# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32638():
    field_value = request.form.get('field', '')
    allowed = {'config.json', 'index.html', 'readme.md'}
    if field_value not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + field_value
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
