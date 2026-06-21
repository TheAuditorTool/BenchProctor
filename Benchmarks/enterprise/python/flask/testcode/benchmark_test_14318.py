# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest14318():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    processed = data[:64]
    return redirect(str(processed))
