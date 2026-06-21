# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import subprocess


def BenchmarkTest36935():
    env_value = os.environ.get('USER_INPUT', '')
    kind = 'json' if str(env_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = env_value
            data = parsed
        case _:
            data = env_value
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
