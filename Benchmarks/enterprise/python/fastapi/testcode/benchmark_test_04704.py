# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest04704(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = xml_value if xml_value else 'default'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return {"updated": True}
