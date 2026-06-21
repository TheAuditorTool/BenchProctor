# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest44839():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    return render_template_string(data)
