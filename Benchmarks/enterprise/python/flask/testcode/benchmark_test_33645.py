# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest33645():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    prefix = ''
    data = prefix + str(graphql_var)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
