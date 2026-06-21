# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest70463():
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    return render_template_string(data)
