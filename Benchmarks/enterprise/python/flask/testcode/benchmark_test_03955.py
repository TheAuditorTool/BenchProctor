# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import json
from flask import request


def BenchmarkTest03955():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    return render_template_string('safe block: {{ value }}', value=data)
