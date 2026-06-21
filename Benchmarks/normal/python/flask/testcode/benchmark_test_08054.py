# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest08054():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return render_template_string(processed)
