# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest29312():
    header_value = request.headers.get('X-Custom-Header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    def _primary():
        return Markup('<div>' + str(data) + '</div>')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
