# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from app_runtime import db


async def BenchmarkTest69775(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = (lambda v: v.strip())(comment_value)
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
