# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request
import asyncio


def BenchmarkTest03504():
    host_value = request.headers.get('Host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = asyncio.run(fetch_payload())
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
