# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest20819(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = default_blank(multipart_value)
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JSONResponse({'token': str(token)}, status_code=200)
