# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest03579():
    origin_value = request.headers.get('Origin', '')
    processed = 'true' if str(origin_value).lower() in ('true', '1', 'yes', 'on') else 'false'
    return render_template_string(processed)
