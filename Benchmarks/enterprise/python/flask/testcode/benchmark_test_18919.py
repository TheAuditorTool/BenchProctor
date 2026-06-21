# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest18919():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = (lambda v: v.strip())(json_value)
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
