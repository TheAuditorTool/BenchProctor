# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest39662():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
