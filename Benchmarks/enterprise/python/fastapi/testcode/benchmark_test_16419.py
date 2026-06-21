# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest16419(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    processed = 'true' if str(xml_value).lower() in ('true', '1', 'yes', 'on') else 'false'
    request.session['data'] = str(processed)
    return {"updated": True}
