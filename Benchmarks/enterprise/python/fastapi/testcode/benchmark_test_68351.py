# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest68351(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    processed = 'true' if str(header_value).lower() in ('true', '1', 'yes', 'on') else 'false'
    request.session['data'] = str(processed)
    return {"updated": True}
