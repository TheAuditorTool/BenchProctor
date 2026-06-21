# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest30035():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header}'
    return render_template_string(data)
