# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import asyncio
from app_runtime import db


def BenchmarkTest20950():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    _ev = {}
    eval(compile("_ev['r'] = render_template_string(data)", '<sink>', 'exec'))
    return _ev['r']
