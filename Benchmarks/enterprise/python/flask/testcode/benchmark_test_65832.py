# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import asyncio


def BenchmarkTest65832(path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
