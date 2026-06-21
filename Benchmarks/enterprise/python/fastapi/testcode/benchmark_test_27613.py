# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest27613(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
