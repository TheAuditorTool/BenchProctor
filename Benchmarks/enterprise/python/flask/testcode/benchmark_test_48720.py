# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
import os
from flask import jsonify


def BenchmarkTest48720():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
