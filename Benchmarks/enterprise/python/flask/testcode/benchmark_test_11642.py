# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def BenchmarkTest11642():
    cookie_value = request.cookies.get('session_token', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(cookie_value)
    data = collected
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
