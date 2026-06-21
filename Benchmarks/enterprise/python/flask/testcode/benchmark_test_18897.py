# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest18897():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    return render_template_string('safe block: {{ value }}', value=json_value)
