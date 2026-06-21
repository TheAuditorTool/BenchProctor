# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest56678(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = xml_value if xml_value else 'default'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
