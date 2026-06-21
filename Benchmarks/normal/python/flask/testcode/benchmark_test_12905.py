# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest12905():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
