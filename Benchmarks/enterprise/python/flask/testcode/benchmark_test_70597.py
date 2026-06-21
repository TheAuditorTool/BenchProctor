# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from urllib.parse import unquote
from flask import request


def BenchmarkTest70597():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return render_template_string(processed)
