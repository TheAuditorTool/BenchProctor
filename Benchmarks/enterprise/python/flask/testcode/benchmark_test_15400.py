# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import jsonify
import os
import asyncio
from app_runtime import db


def BenchmarkTest15400():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    if os.environ.get("APP_ENV", "production") != "test":
        return Markup('<div>' + str(data) + '</div>')
    return jsonify({"result": "success"})
