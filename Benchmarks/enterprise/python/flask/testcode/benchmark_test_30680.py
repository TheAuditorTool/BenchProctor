# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest30680():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    return render_template_string(data)
