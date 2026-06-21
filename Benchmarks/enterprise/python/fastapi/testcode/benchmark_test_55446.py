# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def normalise_input(value):
    return value.strip()

async def BenchmarkTest55446(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = normalise_input(auth_header)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
