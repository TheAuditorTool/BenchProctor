# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest00281():
    cookie_value = request.cookies.get('session_token', '')
    os.environ['APP_USER_PREFERENCE'] = str(cookie_value)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
