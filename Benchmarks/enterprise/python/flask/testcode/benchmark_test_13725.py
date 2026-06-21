# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def ensure_str(value):
    return str(value)

def BenchmarkTest13725():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    processed = str(data).replace("<script", "")
    return Markup('<div>' + str(processed) + '</div>')
