# SPDX-License-Identifier: Apache-2.0
import re
import os
from flask import jsonify
import runpy


def to_text(value):
    return str(value).strip()

def BenchmarkTest46232():
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-{}()=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
