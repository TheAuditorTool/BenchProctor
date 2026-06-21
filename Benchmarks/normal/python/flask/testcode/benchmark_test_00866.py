# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest00866():
    ua_value = request.headers.get('User-Agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    processed = data[:64]
    return Markup('<div>' + str(processed) + '</div>')
