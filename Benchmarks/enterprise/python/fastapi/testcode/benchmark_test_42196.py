# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest42196(request: Request):
    upload_name = (await request.form()).get('upload', '')
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    eval(str(data))
    return {"updated": True}
