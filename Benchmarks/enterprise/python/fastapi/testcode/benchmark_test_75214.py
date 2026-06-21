# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


request_state: dict[str, str] = {}

async def BenchmarkTest75214(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
