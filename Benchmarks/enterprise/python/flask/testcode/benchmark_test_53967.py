# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
import os
from flask import jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest53967():
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
