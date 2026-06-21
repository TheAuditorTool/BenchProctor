# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import markdown
import bleach
import asyncio


def BenchmarkTest64804(path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    processed = bleach.clean(markdown.markdown(data))
    return Markup('<div>' + str(processed) + '</div>')
