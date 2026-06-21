# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def relay_value(value):
    return value

async def BenchmarkTest58516(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = relay_value(forwarded_ip)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
