# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest01107():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    return '<!-- diagnostic build token: ' + str(comment_value) + ' -->', 200, {'Content-Type': 'text/html'}
