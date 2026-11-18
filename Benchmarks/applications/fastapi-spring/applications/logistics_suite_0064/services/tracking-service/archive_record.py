# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/archive_record")
async def archive_record(request: Request):
    transcript = (await request.form()).get('field', '')
    parts = str(transcript).split(',')
    parcel = ' '.join(parts)
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=parcel))
