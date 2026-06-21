# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
import base64
from flask import request


def BenchmarkTest14860():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
