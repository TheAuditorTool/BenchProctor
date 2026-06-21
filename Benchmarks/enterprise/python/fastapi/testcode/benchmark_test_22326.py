# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest22326(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '{}'.format(multipart_value)
    request.session['data'] = str(data)
    return {"updated": True}
