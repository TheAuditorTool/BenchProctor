# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest43276():
    origin_value = request.headers.get('Origin', '')
    return render_template_string(origin_value)
