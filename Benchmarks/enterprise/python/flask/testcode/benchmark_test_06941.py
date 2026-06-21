# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest06941():
    xml_value = request.get_data(as_text=True)
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return render_template_string(processed)
