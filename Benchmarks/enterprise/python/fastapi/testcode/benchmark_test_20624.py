# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from app_runtime import db


async def BenchmarkTest20624(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(comment_value)
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
