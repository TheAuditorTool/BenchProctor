# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import jsonify
import asyncio
from app_runtime import db


def BenchmarkTest26280():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return render_template_string(processed)
