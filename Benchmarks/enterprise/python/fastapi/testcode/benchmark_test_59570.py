# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest59570(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '%s' % (multipart_value,)
    request.session['data'] = str(data)
    return {"updated": True}
