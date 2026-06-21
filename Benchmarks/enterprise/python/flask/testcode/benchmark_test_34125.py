# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def ensure_str(value):
    return str(value)

def BenchmarkTest34125():
    user_id = request.args.get('id', '')
    data = ensure_str(user_id)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return render_template_string(processed)
