# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest23165():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip:.200s}'
    return render_template_string(data)
