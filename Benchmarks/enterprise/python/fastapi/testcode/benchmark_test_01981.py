# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01981(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = (lambda v: v.strip())(upload_name)
    int(str(data))
    return {"updated": True}
