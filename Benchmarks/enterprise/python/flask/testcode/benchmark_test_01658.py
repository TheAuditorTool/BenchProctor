# SPDX-License-Identifier: Apache-2.0
import json
from app_runtime import db


def BenchmarkTest01658():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
