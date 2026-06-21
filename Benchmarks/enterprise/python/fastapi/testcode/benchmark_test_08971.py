# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest08971(request: Request):
    upload_name = (await request.form()).get('upload', '')
    eval(str(upload_name))
    return {"updated": True}
