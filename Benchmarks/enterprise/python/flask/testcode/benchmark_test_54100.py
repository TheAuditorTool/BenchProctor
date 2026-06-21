# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest54100():
    raw_body = request.get_data(as_text=True)
    processed = 'true' if str(raw_body).lower() in ('true', '1', 'yes', 'on') else 'false'
    return render_template_string(processed)
