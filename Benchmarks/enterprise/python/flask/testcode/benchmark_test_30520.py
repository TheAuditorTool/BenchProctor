# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest30520():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
