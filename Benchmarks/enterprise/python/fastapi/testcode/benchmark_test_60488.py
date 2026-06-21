# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle
from app_runtime import mq_client


async def BenchmarkTest60488(request: Request):
    msg_value = mq_client.get_message().body
    pending = list(str(msg_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
