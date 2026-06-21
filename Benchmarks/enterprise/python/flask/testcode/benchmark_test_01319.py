# SPDX-License-Identifier: Apache-2.0
import re
import os
from flask import jsonify


def BenchmarkTest01319():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return jsonify({'validated': str(processed)}), 200
    return jsonify({"result": "success"})
