# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import render_template_string
from app_runtime import db


def BenchmarkTest66609():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = ' '.join(str(comment_value).split())
    return render_template_string('{{ value }}', value=data)
