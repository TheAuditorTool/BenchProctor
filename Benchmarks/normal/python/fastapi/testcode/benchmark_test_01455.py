# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest01455(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    auth_check('user', xml_value)
    return {"updated": True}
