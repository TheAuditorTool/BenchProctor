# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest17183():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = default_blank(graphql_var)
    def _primary():
        return render_template_string(data)
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
