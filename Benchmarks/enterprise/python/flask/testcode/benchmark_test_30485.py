# SPDX-License-Identifier: Apache-2.0
from flask import session
import re
import os
from flask import jsonify


def BenchmarkTest30485():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    session['data'] = str(processed)
    return jsonify({"result": "success"})
