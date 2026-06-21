# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest57649():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
