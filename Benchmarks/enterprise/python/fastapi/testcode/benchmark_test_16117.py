# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest16117(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    request.session['data'] = str(data)
    return {"updated": True}
