# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest31651():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    return render_template_string(data)
