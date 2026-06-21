# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

async def BenchmarkTest53772(request: Request):
    secret_value = 'config_secret_test_abc123'
    data = FormData(payload=secret_value).payload
    auth_check('user', data)
    return {"updated": True}
