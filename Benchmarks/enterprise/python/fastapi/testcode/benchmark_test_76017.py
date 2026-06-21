# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest76017(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
