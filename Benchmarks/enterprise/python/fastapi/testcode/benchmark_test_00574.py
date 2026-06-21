# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest00574(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '{}'.format(comment_value)
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return {"updated": True}
