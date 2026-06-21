# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest13234():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
