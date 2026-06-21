# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest05733():
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
