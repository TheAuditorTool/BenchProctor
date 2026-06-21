# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify
import asyncio


def BenchmarkTest10263():
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
