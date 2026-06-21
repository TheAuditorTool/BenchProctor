# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest46690():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = relay_value(comment_value)
    processed = data[:64]
    return render_template_string(processed)
