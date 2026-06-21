# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import runpy


def BenchmarkTest32473():
    auth_header = request.headers.get('Authorization', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', auth_header):
        return jsonify({'error': 'forbidden'}), 400
    processed = auth_header
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
