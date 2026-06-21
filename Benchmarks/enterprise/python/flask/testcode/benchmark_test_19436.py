# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def to_text(value):
    return str(value).strip()

def BenchmarkTest19436():
    ua_value = request.headers.get('User-Agent', '')
    data = to_text(ua_value)
    return render_template_string('safe block: {{ value }}', value=data)
