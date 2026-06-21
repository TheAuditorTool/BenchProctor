# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest33363(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = f'{xml_value}'
    auth_check('user', data)
    return {"updated": True}
