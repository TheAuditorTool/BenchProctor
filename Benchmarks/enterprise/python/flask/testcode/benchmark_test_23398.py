# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request
import asyncio


def BenchmarkTest23398():
    cookie_value = request.cookies.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        return render_template_string(data)
    return asyncio.run(_evasion_task())
