# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
import os
from flask import jsonify


def BenchmarkTest31545():
    env_value = os.environ.get('USER_INPUT', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(env_value)):
        return jsonify({'error': 'invalid input'}), 400
    processed = env_value
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
