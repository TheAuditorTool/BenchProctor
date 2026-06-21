# SPDX-License-Identifier: Apache-2.0
import requests
from app_runtime import db


def BenchmarkTest42423():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    return '<script src="' + str(comment_value) + '"></script>', 200, {'Content-Type': 'text/html'}
