# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
import os


def BenchmarkTest05763():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
