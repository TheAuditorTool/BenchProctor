# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest05521():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return render_template_string(processed)
