# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import markdown
import bleach
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest00665():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    processed = bleach.clean(markdown.markdown(data))
    return Markup('<div>' + str(processed) + '</div>')
