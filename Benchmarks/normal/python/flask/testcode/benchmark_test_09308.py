# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest09308():
    raw_body = request.get_data(as_text=True)
    parts = []
    for token in str(raw_body).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
