# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
import json
from flask import request


def BenchmarkTest76803():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
