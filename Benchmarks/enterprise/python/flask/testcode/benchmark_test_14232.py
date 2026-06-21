# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest14232():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
