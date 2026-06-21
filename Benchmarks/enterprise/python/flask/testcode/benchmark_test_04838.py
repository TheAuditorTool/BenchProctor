# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest04838():
    cookie_value = request.cookies.get('session_token', '')
    data = '{}'.format(cookie_value)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
