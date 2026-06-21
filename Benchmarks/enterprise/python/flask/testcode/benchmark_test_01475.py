# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import asyncio


def BenchmarkTest01475():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    async def fetch_payload():
        await asyncio.sleep(0)
        return query_array
    data = asyncio.run(fetch_payload())
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
