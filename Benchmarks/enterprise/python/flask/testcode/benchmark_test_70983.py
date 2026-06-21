# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
import os
from flask import jsonify


def BenchmarkTest70983():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
