# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest69623():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value}'
    return render_template_string(data)
