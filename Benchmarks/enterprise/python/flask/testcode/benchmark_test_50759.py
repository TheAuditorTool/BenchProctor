# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest50759():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    return render_template_string(data)
