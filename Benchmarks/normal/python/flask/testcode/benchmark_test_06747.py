# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest06747():
    upload_name = request.files['upload'].filename
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    return render_template_string('safe block: {{ value }}', value=data)
