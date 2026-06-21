# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from urllib.parse import unquote
from flask import request


def BenchmarkTest49217():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    return render_template_string(data)
