# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/publish_manifest")
async def publish_manifest(request: Request):
    preface = request.cookies.get('session_token', '')
    parts = str(preface).split(',')
    addendum = ' '.join(parts)
    parsed = json.loads(addendum)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
