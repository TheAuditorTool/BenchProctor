# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest04750():
    multipart_value = request.form.get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    def _primary():
        return render_template_string(data)
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
