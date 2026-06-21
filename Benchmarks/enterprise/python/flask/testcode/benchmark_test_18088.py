# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest18088():
    auth_header = request.headers.get('Authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    processed = data[:64]
    return Markup('<div>' + str(processed) + '</div>')
