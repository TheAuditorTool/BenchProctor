# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest05557():
    user_id = request.args.get('id', '')
    processed = 'true' if str(user_id).lower() in ('true', '1', 'yes', 'on') else 'false'
    return render_template_string(processed)
