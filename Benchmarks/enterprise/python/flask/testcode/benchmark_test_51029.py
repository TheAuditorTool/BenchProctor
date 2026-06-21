# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest51029():
    xml_value = request.get_data(as_text=True)
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    def _primary():
        return Markup('<img src="' + str(data) + '">')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
