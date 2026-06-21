# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest05893():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value}'
    return render_template_string(data)
