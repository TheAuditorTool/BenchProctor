# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest06004():
    auth_header = request.headers.get('Authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
