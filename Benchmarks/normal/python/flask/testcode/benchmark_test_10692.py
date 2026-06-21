# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest10692():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
