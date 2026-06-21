# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
import os
from flask import jsonify


def BenchmarkTest04439():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return jsonify({"result": "success"})
