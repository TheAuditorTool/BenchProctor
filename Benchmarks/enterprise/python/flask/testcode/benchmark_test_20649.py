# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from urllib.parse import unquote
from flask import request


def BenchmarkTest20649():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
