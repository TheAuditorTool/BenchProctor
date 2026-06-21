# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest13173():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    return render_template_string(data)
