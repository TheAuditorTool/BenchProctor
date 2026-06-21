# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
import os
from flask import jsonify


def BenchmarkTest17539():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
