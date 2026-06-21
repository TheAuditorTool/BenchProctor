# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request
import asyncio


def BenchmarkTest62902():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = asyncio.run(fetch_payload())
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
