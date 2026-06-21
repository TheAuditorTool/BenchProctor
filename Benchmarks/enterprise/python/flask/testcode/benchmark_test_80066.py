# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest80066():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    _ev = {}
    eval(compile("_ev['r'] = render_template_string(data)", '<sink>', 'exec'))
    return _ev['r']
