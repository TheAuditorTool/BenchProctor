# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
import os


def BenchmarkTest36548():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
