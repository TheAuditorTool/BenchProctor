# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import urllib.parse
from app_runtime import db


def BenchmarkTest58932():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(comment_value)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
