# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest02004(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name:.200s}'
    eval(str(data))
    return {"updated": True}
