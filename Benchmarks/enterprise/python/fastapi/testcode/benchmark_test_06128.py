# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest06128(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value:.200s}'
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return {"updated": True}
