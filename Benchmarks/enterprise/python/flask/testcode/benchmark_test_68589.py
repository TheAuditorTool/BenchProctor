# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request
import asyncio


def BenchmarkTest68589():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = asyncio.run(fetch_payload())
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
