# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


request_state: dict[str, str] = {}

def BenchmarkTest07354():
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
