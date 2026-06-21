# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest35109(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = (lambda v: v.strip())(upload_name)
    eval(str(data))
    return {"updated": True}
