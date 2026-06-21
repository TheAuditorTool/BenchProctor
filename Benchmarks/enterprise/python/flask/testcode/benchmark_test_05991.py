# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from app_runtime import db


def BenchmarkTest05991():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value:.200s}'
    return redirect(str(data))
