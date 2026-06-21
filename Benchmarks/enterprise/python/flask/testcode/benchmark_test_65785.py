# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest65785():
    header_value = request.headers.get('X-Custom-Header', '')
    return render_template_string(header_value)
