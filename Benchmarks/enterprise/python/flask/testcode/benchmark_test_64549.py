# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from app_runtime import db


def BenchmarkTest64549():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = ' '.join(str(comment_value).split())
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return render_template_string(processed)
