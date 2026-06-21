# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest55783():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    return render_template_string(data)
