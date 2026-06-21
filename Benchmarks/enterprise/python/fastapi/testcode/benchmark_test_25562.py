# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from dataclasses import dataclass
from app_runtime import redis_client


@dataclass
class FormData:
    payload: str

async def BenchmarkTest25562(request: Request):
    redis_value = redis_client.get('user_data')
    data = FormData(payload=redis_value).payload
    yaml.safe_load(data)
    return {"updated": True}
