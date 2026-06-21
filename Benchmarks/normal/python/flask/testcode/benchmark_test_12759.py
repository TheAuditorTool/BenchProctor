# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest12759():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = (lambda v: v.strip())(json_value)
    return render_template_string(data)
