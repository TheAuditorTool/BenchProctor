# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest27626(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '%s' % (upload_name,)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
