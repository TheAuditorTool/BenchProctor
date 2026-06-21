# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest41020(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    eval(str(data))
    return {"updated": True}
