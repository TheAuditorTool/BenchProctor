# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import time
import ast


async def BenchmarkTest77831(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    if time.time() > 1000000000:
        requests.get(str(data))
    return {"updated": True}
