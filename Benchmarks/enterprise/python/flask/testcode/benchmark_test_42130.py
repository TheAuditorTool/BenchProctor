# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest42130():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    return render_template_string(data)
