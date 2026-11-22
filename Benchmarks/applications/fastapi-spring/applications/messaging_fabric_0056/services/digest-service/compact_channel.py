# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/compact_channel")
async def compact_channel(request: Request):
    footnote = request.query_params.get('id', '')
    parts = []
    for token in str(footnote).split(','):
        parts.append(token.strip())
    bulletin = ','.join(parts)
    return HTMLResponse('<div>' + str(bulletin) + '</div>')
