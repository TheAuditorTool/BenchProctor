# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import json
from app_runtime import ssm_client


async def BenchmarkTest21909(request: Request):
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    try:
        data = json.loads(ssm_value).get('value', ssm_value)
    except (json.JSONDecodeError, AttributeError):
        data = ssm_value
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
