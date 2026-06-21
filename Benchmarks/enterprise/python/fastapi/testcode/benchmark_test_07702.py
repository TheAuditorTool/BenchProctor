# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest07702(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data, _sep, _rest = str(upload_name).partition('\x00')
    eval(str(data))
    return {"updated": True}
