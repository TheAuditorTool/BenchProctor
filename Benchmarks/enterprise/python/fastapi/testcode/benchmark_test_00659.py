# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest00659(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    eval(str(data))
    return {"updated": True}
