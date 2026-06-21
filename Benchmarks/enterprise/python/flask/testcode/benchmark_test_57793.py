# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
from flask import render_template_string


request_state: dict[str, str] = {}

def BenchmarkTest57793():
    header_value = request.headers.get('X-Custom-Header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    return render_template_string('{{ value }}', value=data)
