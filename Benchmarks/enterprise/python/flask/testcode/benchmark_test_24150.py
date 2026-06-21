# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request
import asyncio


def BenchmarkTest24150():
    host_value = request.headers.get('Host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = asyncio.run(fetch_payload())
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return render_template_string(processed)
