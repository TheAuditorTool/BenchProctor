# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def coalesce_blank(value):
    return value or ''

def BenchmarkTest71935():
    header_value = request.headers.get('X-Custom-Header', '')
    data = coalesce_blank(header_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return render_template_string(processed)
