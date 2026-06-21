# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest30993():
    header_value = request.headers.get('X-Custom-Header', '')
    os.environ['APP_USER_PREFERENCE'] = str(header_value)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
