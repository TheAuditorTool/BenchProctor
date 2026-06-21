# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05176(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = upload_name if upload_name else 'default'
    exec(str(data))
    return {"updated": True}
