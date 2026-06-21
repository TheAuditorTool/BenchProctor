# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
import os
from flask import jsonify


def BenchmarkTest11806():
    env_value = os.environ.get('USER_INPUT', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', env_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = env_value
    return Markup('<div>' + str(processed) + '</div>')
