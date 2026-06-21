# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39510(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    request.session['data'] = str(multipart_value)
    return {"updated": True}
