# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest56458():
    raw_body = request.get_data(as_text=True)
    return render_template_string('safe block: {{ value }}', value=raw_body)
