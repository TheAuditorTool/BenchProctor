# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest81423():
    field_value = request.form.get('field', '')
    data = ensure_str(field_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
