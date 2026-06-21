# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest64902():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    return render_template_string(data)
