# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest71626():
    field_value = request.form.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    processed = data[:64]
    return Markup('<div>' + str(processed) + '</div>')
