# SPDX-License-Identifier: Apache-2.0
import requests
from app_runtime import db


def BenchmarkTest12214():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    kind = 'json' if str(comment_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = comment_value
            data = parsed
        case _:
            data = comment_value
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
