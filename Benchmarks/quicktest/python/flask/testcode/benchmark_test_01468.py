# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest01468():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    parts = str(json_value).split(',')
    data = ','.join(parts)
    return render_template_string(data)
