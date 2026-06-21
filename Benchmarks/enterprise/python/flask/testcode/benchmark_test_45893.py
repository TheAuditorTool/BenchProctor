# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest45893():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    os.environ['APP_USER_PREFERENCE'] = str(json_value)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
