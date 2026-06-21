# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


request_state: dict[str, str] = {}

def BenchmarkTest35563():
    xml_value = request.get_data(as_text=True)
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    processed = data[:64]
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
