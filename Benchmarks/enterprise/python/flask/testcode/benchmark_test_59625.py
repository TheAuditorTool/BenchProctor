# SPDX-License-Identifier: Apache-2.0
import requests
from app_runtime import db


def BenchmarkTest59625():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '{}'.format(comment_value)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
