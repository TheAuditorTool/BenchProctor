# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest20464():
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    return Markup('<div>' + str(data) + '</div>')
