# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest10925():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    return render_template_string(data)
