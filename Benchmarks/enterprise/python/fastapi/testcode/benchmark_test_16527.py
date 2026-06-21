# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle
from app_runtime import mq_client


async def BenchmarkTest16527(request: Request):
    msg_value = mq_client.get_message().body
    data = (lambda v: v.strip())(msg_value)
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
