# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def normalise_input(value):
    return value.strip()

async def BenchmarkTest62544(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = normalise_input(cookie_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
