# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest75024():
    ua_value = request.headers.get('User-Agent', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(ua_value)
    data = collected
    return render_template_string('safe block: {{ value }}', value=data)
