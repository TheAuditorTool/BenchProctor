# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest29429():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
