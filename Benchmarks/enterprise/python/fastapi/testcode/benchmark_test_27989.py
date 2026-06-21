# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle
from app_runtime import mq_client


async def BenchmarkTest27989(request: Request):
    msg_value = mq_client.get_message().body
    data = msg_value if msg_value else 'default'
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
