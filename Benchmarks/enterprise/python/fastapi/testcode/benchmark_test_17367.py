# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def ensure_str(value):
    return str(value)

async def BenchmarkTest17367(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = ensure_str(upload_name)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
