# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest44656(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
