# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
import os
import asyncio


def BenchmarkTest54801():
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
