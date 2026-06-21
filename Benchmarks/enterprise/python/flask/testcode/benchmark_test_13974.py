# SPDX-License-Identifier: Apache-2.0
import os
from flask import redirect
import urllib.parse


request_state: dict[str, str] = {}

def BenchmarkTest13974():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    processed = data[:64]
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
