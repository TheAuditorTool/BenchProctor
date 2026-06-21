# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from app_runtime import db


async def BenchmarkTest64304(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = []
    for token in str(comment_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
