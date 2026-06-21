# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest25190():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    return render_template_string(data)
