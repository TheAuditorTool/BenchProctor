# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from app_runtime import mq_client


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest28325(request: Request):
    msg_value = mq_client.get_message().body
    reader = make_reader(msg_value)
    data = reader()
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
