# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest08638():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
