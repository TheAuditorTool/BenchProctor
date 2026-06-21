# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import runpy


def BenchmarkTest03079():
    header_value = request.headers.get('X-Custom-Header', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', header_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = header_value
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
