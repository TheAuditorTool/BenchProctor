# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest05997():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
