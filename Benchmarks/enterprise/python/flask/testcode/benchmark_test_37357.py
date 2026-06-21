# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
import asyncio


def BenchmarkTest37357(path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
