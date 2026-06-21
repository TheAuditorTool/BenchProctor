# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle
from app_runtime import db


async def BenchmarkTest13216(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if comment_value:
        data = comment_value
    else:
        data = ''
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
