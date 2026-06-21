# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
import asyncio


def BenchmarkTest50856():
    cookie_value = request.cookies.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    return Markup('<div>' + str(processed) + '</div>')
