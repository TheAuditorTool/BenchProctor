# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest78083(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = ' '.join(str(upload_name).split())
    eval(str(data))
    return {"updated": True}
