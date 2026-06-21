# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest11370():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '{}'.format(json_value)
    return render_template_string(data)
