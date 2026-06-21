# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest68826(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = str(upload_name).replace('\x00', '')
    result = 100 / int(str(data))
    return {"updated": True}
