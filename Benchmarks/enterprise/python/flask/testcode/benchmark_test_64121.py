# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest64121():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    return Markup('<div>' + str(graphql_var) + '</div>')
