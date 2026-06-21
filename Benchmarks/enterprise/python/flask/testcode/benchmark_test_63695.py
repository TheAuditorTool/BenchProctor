# SPDX-License-Identifier: Apache-2.0
import requests
import re
import os
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest63695():
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
