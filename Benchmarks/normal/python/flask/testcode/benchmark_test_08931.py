# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import runpy


def BenchmarkTest08931():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
