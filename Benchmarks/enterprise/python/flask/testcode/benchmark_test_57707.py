# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest57707():
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
