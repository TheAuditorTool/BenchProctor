# SPDX-License-Identifier: Apache-2.0
from flask import request
import json


def BenchmarkTest63133():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    try:
        data = json.loads(graphql_var).get('value', graphql_var)
    except (json.JSONDecodeError, AttributeError):
        data = graphql_var
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
