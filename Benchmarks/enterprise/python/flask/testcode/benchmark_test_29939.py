# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import base64
from flask import request


def BenchmarkTest29939():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    return render_template_string(data)
