# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from app_runtime import db


async def BenchmarkTest51078(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % (comment_value,)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
