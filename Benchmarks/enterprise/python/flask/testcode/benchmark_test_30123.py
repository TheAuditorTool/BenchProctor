# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest30123():
    cookie_value = request.cookies.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
