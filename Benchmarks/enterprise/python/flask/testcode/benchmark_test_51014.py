# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def BenchmarkTest51014():
    cookie_value = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
