# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest08374():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    return render_template_string(data)
