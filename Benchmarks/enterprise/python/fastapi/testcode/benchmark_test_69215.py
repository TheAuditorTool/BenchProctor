# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest69215(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '%s' % str(multipart_value)
    eval(str(data))
    return {"updated": True}
