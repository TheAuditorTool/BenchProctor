# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def normalise_input(value):
    return value.strip()

async def BenchmarkTest35658(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = normalise_input(forwarded_ip)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
