# SPDX-License-Identifier: Apache-2.0
import os
import json
from flask import request, jsonify


def BenchmarkTest33389():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
