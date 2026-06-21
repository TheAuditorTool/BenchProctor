# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest60664(request: Request):
    upload_name = (await request.form()).get('upload', '')
    defusedxml.ElementTree.fromstring(str(upload_name))
    return {"updated": True}
