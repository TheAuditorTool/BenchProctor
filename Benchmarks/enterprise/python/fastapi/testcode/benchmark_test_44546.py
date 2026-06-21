# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import ast


async def BenchmarkTest44546(request: Request):
    upload_name = (await request.form()).get('upload', '')
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    async def _evasion_task():
        _resp = requests.get(str(data))
        exec(_resp.text)
    await _evasion_task()
    return {"updated": True}
