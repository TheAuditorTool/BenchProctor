# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest37644():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
