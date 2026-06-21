# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest16304(request: Request):
    upload_name = (await request.form()).get('upload', '')
    if upload_name:
        data = upload_name
    else:
        data = ''
    exec(str(data))
    return {"updated": True}
