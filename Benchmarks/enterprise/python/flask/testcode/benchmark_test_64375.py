# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest64375():
    cookie_value = request.cookies.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
