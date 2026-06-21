# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest19539(request: Request):
    upload_name = (await request.form()).get('upload', '')
    prefix = ''
    data = prefix + str(upload_name)
    exec(str(data))
    return {"updated": True}
