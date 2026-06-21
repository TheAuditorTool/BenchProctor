# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01464(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = (lambda v: v.strip())(upload_name)
    exec(str(data))
    return {"updated": True}
