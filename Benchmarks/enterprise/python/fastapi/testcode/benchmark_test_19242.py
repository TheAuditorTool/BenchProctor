# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from app_runtime import db


def normalise_input(value):
    return value.strip()

async def BenchmarkTest19242(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = normalise_input(comment_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return {"updated": True}
