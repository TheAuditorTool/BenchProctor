# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request
import asyncio


def BenchmarkTest02107():
    header_value = request.headers.get('X-Custom-Header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = asyncio.run(fetch_payload())
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
