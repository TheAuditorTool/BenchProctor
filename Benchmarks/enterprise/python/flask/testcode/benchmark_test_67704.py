# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
from flask import render_template_string
import asyncio


def BenchmarkTest67704():
    user_id = request.args.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = asyncio.run(fetch_payload())
    return render_template_string('{{ value }}', value=data)
