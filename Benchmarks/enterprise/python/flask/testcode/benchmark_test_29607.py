# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest29607():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    return render_template_string(data)
