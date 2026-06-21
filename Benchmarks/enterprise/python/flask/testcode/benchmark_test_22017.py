# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest22017():
    multipart_value = request.form.get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
