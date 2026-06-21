# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest02411():
    cookie_value = request.cookies.get('session_token', '')
    processed = html.escape(cookie_value)
    return Markup('<div>' + str(processed) + '</div>')
