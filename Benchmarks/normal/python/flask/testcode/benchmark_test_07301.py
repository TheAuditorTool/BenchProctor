# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest07301():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = default_blank(comment_value)
    processed = data[:64]
    return render_template_string(processed)
