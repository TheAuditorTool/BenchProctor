# SPDX-License-Identifier: Apache-2.0
import re
import os
from flask import jsonify
from flask import redirect
import urllib.parse


def BenchmarkTest35390():
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
