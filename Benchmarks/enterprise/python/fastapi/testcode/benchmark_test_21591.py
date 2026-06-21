# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest21591(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '%s' % str(upload_name)
    result = 100 / int(str(data))
    return {"updated": True}
