# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest32514():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    return render_template_string(data)
