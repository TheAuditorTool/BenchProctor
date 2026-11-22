# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/publish_snapshot")
async def publish_snapshot(request: Request):
    summary = request.query_params.get('id', '')
    parts = []
    for token in str(summary).split(','):
        parts.append(token.strip())
    phrase = ','.join(parts)
    return HTMLResponse('<div>' + str(phrase) + '</div>')
