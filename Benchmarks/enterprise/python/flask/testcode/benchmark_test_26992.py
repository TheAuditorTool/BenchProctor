# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest26992():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = '%s' % str(graphql_var)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
