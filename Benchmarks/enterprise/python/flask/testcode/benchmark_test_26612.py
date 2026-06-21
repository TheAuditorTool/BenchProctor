# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest26612():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    return render_template_string(data)
