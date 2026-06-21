# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest16020():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    return render_template_string(data)
