# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import html
from app_runtime import db


def relay_value(value):
    return value

async def BenchmarkTest04138(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = relay_value(comment_value)
    processed = str(data).replace("<script", "")
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return {"updated": True}
