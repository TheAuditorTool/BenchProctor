# SPDX-License-Identifier: Apache-2.0
import os
import sys
from flask import jsonify
import asyncio


def BenchmarkTest29101():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    async def fetch_payload():
        await asyncio.sleep(0)
        return argv_value
    data = asyncio.run(fetch_payload())
    checked_path = os.path.normpath(data)
    os.unlink('/var/app/data/' + str(checked_path))
    return jsonify({"result": "success"})
