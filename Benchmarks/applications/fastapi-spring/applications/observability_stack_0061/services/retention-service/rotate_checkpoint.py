# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/rotate_checkpoint")
async def rotate_checkpoint(request: Request):
    headline = request.cookies.get('session_token', '')
    cohort = headline if headline else 'default'
    return HTMLResponse('<div>' + str(cohort) + '</div>')
