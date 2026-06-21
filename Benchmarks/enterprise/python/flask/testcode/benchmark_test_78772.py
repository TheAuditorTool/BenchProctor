# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
import os
from flask import jsonify


def BenchmarkTest78772():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return render_template_string(processed)
