# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest31114():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
