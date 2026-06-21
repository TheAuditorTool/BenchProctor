# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def ensure_str(value):
    return str(value)

def BenchmarkTest32463():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
