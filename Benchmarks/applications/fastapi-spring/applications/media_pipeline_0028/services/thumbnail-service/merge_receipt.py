# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/merge_receipt")
async def merge_receipt(request: Request):
    citation = (await request.json()).get('payload', '')
    reader = make_reader(citation)
    rendition = reader()
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(rendition))
    return HTMLResponse(page)
