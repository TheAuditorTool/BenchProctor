# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def to_text(value):
    return str(value).strip()

def BenchmarkTest25574():
    upload_name = request.files['upload'].filename
    data = to_text(upload_name)
    return render_template_string('safe block: {{ value }}', value=data)
