# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest02792():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return render_template_string(processed)
