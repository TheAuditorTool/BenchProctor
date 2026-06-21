# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest30870():
    ua_value = request.headers.get('User-Agent', '')
    processed = html.escape(ua_value)
    return Markup('<div>' + str(processed) + '</div>')
