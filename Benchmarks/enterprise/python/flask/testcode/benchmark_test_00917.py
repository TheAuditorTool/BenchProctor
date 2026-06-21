# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest00917():
    cookie_value = request.cookies.get('session_token', '')
    kind = 'json' if str(cookie_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = cookie_value
            data = parsed
        case _:
            data = cookie_value
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
