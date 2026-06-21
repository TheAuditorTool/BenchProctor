# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request
import asyncio


def BenchmarkTest24442():
    origin_value = request.headers.get('Origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = asyncio.run(fetch_payload())
    processed = str(data).replace("<script", "")
    return Markup('<div>' + str(processed) + '</div>')
