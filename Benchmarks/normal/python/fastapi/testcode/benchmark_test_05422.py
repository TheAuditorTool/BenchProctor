# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest05422(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(comment_value)
    data = reader()
    os.remove(str(data))
    return {"updated": True}
