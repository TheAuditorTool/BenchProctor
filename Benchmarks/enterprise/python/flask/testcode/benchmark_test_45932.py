# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from app_runtime import db


def BenchmarkTest45932():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = (lambda v: v.strip())(comment_value)
    return redirect(str(data))
