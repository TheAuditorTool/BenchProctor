# SPDX-License-Identifier: Apache-2.0
import requests
from app_runtime import db


def BenchmarkTest42319():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(comment_value).split(',')
    data = ','.join(parts)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
