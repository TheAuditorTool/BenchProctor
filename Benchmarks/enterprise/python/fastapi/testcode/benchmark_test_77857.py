# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import ast


async def BenchmarkTest77857(request: Request):
    referer_value = request.headers.get('referer', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    yaml.safe_load(data)
    return {"updated": True}
