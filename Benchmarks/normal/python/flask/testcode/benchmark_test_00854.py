# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
import os
from flask import jsonify


def BenchmarkTest00854():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return render_template_string(processed)
