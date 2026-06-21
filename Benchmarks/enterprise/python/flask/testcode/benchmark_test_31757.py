# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest31757():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = default_blank(graphql_var)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
