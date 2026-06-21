# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest27683():
    host_value = request.headers.get('Host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    return render_template_string('safe block: {{ value }}', value=data)
