# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def ensure_str(value):
    return str(value)

def BenchmarkTest55365():
    upload_name = request.files['upload'].filename
    data = ensure_str(upload_name)
    processed = data[:64]
    return render_template_string(processed)
