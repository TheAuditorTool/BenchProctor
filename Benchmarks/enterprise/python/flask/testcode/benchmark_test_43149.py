# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest43149():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = f'{graphql_var:.200s}'
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
