# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest16335():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = ensure_str(json_value)
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
