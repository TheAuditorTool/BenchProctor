# SPDX-License-Identifier: Apache-2.0
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest51010():
    multipart_value = request.form.get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
