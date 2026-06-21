# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest70817(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = (lambda v: v.strip())(upload_name)
    result = 100 / int(str(data))
    return {"updated": True}
