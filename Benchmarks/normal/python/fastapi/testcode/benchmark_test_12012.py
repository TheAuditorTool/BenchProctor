# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import runpy
from app_runtime import db


async def BenchmarkTest12012(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(comment_value) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
