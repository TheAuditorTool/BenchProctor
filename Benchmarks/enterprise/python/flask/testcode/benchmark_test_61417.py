# SPDX-License-Identifier: Apache-2.0
import requests
import json
from flask import request


def BenchmarkTest61417():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
