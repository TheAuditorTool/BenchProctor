# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest77674():
    raw_body = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return render_template_string(processed)
