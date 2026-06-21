# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import base64
from flask import request


def BenchmarkTest19526():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    return render_template_string('safe block: {{ value }}', value=data)
