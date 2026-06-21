# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import os


def relay_value(value):
    return value

def BenchmarkTest07156():
    auth_header = request.headers.get('Authorization', '')
    data = relay_value(auth_header)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
