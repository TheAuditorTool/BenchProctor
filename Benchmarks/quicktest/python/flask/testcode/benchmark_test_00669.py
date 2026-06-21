# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from urllib.parse import unquote
from flask import request


def BenchmarkTest00669():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    return Markup('<div>' + str(data) + '</div>')
