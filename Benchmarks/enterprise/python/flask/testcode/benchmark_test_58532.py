# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import runpy


def to_text(value):
    return str(value).strip()

def BenchmarkTest58532():
    multipart_value = request.form.get('multipart_field', '')
    data = to_text(multipart_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
