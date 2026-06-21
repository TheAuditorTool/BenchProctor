# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest69971():
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
