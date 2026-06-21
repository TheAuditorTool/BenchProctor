# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest04555(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    defusedxml.ElementTree.fromstring(str(header_value))
    return {"updated": True}
