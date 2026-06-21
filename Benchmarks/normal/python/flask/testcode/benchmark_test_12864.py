# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest12864():
    multipart_value = request.form.get('multipart_field', '')
    data = handle(multipart_value)
    if not re.fullmatch('^[\\w\\s<>\\"\'/(){}.*]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
