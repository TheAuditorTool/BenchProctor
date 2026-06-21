# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest30002():
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
