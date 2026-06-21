# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest02784(request: Request):
    upload_name = (await request.form()).get('upload', '')
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
