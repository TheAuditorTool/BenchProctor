# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest10942(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = f'{xml_value:.200s}'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
