# SPDX-License-Identifier: Apache-2.0
import re
import os
from flask import jsonify


def BenchmarkTest76792():
    env_value = os.environ.get('USER_INPUT', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', env_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = env_value
    eval(str(processed))
    return jsonify({"result": "success"})
