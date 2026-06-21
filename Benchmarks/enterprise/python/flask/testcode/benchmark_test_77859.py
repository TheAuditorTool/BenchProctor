# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from urllib.parse import unquote
from flask import request


def BenchmarkTest77859():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
