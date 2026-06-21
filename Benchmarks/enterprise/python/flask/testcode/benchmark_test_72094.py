# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest72094():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = '{}'.format(graphql_var)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
