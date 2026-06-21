# SPDX-License-Identifier: Apache-2.0
import subprocess
import os
from flask import jsonify


def BenchmarkTest08854():
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
