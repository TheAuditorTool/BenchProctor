# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def to_text(value):
    return str(value).strip()

def BenchmarkTest39686():
    field_value = request.form.get('field', '')
    data = to_text(field_value)
    return render_template_string('safe block: {{ value }}', value=data)
