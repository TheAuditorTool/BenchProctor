# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle
from app_runtime import mq_client


def relay_value(value):
    return value

async def BenchmarkTest51220(request: Request):
    msg_value = mq_client.get_message().body
    data = relay_value(msg_value)
    async def _evasion_task():
        pickle.loads(data.encode('latin-1'))
    await _evasion_task()
    return {"updated": True}
