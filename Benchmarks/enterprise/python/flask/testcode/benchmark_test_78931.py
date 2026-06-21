# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest78931():
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
