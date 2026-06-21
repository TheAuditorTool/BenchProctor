# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest77296():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    parts = str(forwarded_ip).split(',')
    data = ','.join(parts)
    return render_template_string(data)
