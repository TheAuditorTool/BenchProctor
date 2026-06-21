# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest66116(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '%s' % (upload_name,)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
