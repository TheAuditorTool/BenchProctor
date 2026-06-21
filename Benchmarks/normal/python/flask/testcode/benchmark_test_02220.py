# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest02220():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
