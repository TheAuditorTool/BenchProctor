# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request
import asyncio


def BenchmarkTest18996():
    upload_name = request.files['upload'].filename
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = asyncio.run(fetch_payload())
    processed = str(data).replace("<script", "")
    return Markup('<img src="' + str(processed) + '">')
