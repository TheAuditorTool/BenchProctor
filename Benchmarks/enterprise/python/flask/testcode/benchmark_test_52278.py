# SPDX-License-Identifier: Apache-2.0
import json
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest52278():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
