# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest73090(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = f'{xml_value:.200s}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
