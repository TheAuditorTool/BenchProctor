# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest00635():
    header_value = request.headers.get('X-Custom-Header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
