# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest31322(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    if not str(xml_value).isdigit():
        raise ValueError('invalid input: ' + str(xml_value))
    return {"updated": True}
