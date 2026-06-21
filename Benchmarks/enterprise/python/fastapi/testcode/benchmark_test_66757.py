# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest66757(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = coalesce_blank(auth_header)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
