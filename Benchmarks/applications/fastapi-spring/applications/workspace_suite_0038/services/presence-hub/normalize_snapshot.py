# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/normalize_snapshot")
async def normalize_snapshot(request: Request):
    preface = request.cookies.get('session_token', '')
    remark = preface if preface else 'default'
    return HTMLResponse('<div>' + str(remark) + '</div>')
