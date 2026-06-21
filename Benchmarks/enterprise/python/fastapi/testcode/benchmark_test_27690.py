# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest27690(request: Request):
    user_id = request.query_params.get('id', '')
    data = normalise_input(user_id)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
