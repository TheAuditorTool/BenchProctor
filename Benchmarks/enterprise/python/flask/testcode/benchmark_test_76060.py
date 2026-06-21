# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest76060():
    auth_header = request.headers.get('Authorization', '')
    return render_template_string(auth_header)
