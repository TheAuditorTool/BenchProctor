# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest39038():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = str(graphql_var).replace('\x00', '')
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
