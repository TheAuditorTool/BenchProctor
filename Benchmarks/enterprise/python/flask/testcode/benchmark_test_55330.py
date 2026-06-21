# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import asyncio
import ctypes
from app_runtime import db


def BenchmarkTest55330():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
