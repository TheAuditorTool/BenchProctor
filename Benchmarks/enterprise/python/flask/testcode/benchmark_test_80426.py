# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest80426():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    return render_template_string(graphql_var)
