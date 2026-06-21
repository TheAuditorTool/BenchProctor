# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest70141():
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    return jsonify({'error': 'An internal error occurred'}), 500
