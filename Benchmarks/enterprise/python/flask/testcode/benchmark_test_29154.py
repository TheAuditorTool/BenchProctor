# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import os
from flask import jsonify


def BenchmarkTest29154():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
