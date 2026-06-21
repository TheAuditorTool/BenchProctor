# SPDX-License-Identifier: Apache-2.0
import re
import json
from flask import request, jsonify
import runpy


def BenchmarkTest67247():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
