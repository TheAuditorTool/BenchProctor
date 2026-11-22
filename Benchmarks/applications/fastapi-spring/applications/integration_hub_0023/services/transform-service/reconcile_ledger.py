# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/reconcile_ledger")
async def reconcile_ledger(request: Request):
    caption = (await request.body()).decode('utf-8')
    handshake = f'{caption!s}'
    with open('/var/app/data/' + str(handshake), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
