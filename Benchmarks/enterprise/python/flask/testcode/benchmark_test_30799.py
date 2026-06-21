# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest30799():
    host_value = request.headers.get('Host', '')
    return render_template_string(host_value)
