# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import jsonify


def BenchmarkTest06786(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
