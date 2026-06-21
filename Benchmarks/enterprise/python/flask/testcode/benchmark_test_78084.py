# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
from flask import render_template_string


def BenchmarkTest78084():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    return render_template_string('{{ value }}', value=data)
