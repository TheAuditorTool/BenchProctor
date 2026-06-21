# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest18057():
    field_value = request.form.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
