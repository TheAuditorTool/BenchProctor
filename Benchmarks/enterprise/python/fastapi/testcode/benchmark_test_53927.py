# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json
import ast
from app_runtime import mq_client


async def BenchmarkTest53927(request: Request):
    msg_value = mq_client.get_message().body
    try:
        data = str(ast.literal_eval(msg_value))
    except (ValueError, SyntaxError):
        data = msg_value
    yaml.safe_load(data)
    return {"updated": True}
