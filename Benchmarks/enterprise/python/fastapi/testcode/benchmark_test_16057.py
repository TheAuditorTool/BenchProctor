# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest16057(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    eval(str(data))
    return {"updated": True}
