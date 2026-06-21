# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest33287():
    upload_name = request.files['upload'].filename
    processed = 'true' if str(upload_name).lower() in ('true', '1', 'yes', 'on') else 'false'
    return render_template_string(processed)
