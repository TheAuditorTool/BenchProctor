# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest07828():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
