# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest07393():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = '%s' % (graphql_var,)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
