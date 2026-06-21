# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import mq_client


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest38743(request: Request):
    msg_value = mq_client.get_message().body
    reader = make_reader(msg_value)
    data = reader()
    json.loads(data)
    return {"updated": True}
