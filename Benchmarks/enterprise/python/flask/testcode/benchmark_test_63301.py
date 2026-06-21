# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import jsonify


def BenchmarkTest63301(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return render_template_string(processed)
