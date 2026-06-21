# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
from flask import render_template_string


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest25541():
    field_value = request.form.get('field', '')
    data = default_blank(field_value)
    return render_template_string('{{ value }}', value=data)
