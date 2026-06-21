# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request
import asyncio


def BenchmarkTest04396():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
