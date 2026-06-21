# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import ast
import asyncio
from app_runtime import db


def BenchmarkTest43065():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    async def _evasion_task():
        return Markup('<div>' + str(data) + '</div>')
    return asyncio.run(_evasion_task())
