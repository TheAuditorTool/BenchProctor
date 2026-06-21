# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request
import asyncio


def BenchmarkTest45004():
    ua_value = request.headers.get('User-Agent', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = asyncio.run(fetch_payload())
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
