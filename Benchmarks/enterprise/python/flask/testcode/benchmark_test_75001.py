# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import asyncio
import pickle
from app_runtime import mq_client


def coalesce_blank(value):
    return value or ''

def BenchmarkTest75001():
    msg_value = mq_client.get_message().body
    data = coalesce_blank(msg_value)
    async def _evasion_task():
        pickle.loads(data.encode('latin-1'))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
