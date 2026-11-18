# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import PlainTextResponse
import json


router = APIRouter()


@router.post("/normalize_ledger")
async def normalize_ledger(request: Request):
    subject = getattr((await request.form()).get('upload'), 'filename', '')
    try:
        ledger = json.loads(subject).get('value', subject)
    except (json.JSONDecodeError, AttributeError):
        ledger = subject
    with open('/var/app/data/' + str(ledger), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
