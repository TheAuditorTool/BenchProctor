# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/publish_schedule")
async def publish_schedule(request: Request):
    preface = (await request.form()).get('field', '')
    parts = str(preface).split(',')
    remark = ' '.join(parts)
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=remark))
