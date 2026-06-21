# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest70277():
    field_value = request.form.get('field', '')
    data = '%s' % str(field_value)
    return render_template_string(data)
