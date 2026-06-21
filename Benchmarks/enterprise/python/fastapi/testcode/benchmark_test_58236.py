# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


request_state: dict[str, str] = {}

async def BenchmarkTest58236(request: Request):
    upload_name = (await request.form()).get('upload', '')
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
