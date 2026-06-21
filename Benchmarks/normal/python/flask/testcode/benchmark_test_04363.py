# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from app_runtime import db


def BenchmarkTest04363():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    return render_template_string(comment_value)
