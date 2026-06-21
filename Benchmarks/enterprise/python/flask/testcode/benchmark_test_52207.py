# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import re


def coalesce_blank(value):
    return value or ''

def BenchmarkTest52207():
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    processed = data[:64]
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return jsonify({'validated': str(processed)}), 200
    return jsonify({"result": "success"})
