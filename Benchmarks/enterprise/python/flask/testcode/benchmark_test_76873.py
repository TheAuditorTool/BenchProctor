# SPDX-License-Identifier: Apache-2.0
import requests
from app_runtime import db


def BenchmarkTest76873():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    pending = list(str(comment_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
