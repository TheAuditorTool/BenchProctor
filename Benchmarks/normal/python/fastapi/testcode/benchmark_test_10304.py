# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def to_text(value):
    return str(value).strip()

async def BenchmarkTest10304(request: Request):
    user_id = request.query_params.get('id', '')
    data = to_text(user_id)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
