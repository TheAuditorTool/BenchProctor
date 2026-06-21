# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest17036():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    return render_template_string('safe block: {{ value }}', value=data)
