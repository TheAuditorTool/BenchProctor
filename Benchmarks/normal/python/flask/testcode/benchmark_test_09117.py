# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import runpy


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest09117():
    ua_value = request.headers.get('User-Agent', '')
    reader = make_reader(ua_value)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
