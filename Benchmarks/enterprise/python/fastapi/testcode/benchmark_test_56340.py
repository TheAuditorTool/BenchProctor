# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def normalise_input(value):
    return value.strip()

async def BenchmarkTest56340(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = normalise_input(ua_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    request.session['data'] = str(processed)
    return {"updated": True}
