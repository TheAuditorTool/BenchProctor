# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def relay_value(value):
    return value

async def BenchmarkTest54574(request: Request):
    user_id = request.query_params.get('id', '')
    data = relay_value(user_id)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
