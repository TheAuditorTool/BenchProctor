# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest24873():
    auth_header = request.headers.get('Authorization', '')
    data = ensure_str(auth_header)
    processed = data[:64]
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
