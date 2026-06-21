# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import render_template_string
from app_runtime import db


def BenchmarkTest51767():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '{}'.format(comment_value)
    return render_template_string('{{ value }}', value=data)
