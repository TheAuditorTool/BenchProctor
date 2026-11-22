# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from security import require_login


router = APIRouter()


@router.post("/index_document")
@require_login
async def index_document(request: Request):
    footnote = request.headers.get('x-custom-header', '')
    addendum = '%s' % (footnote,)
    requests.post("http://convert-service:8080/RunConversion", json={"documents_payload": str(addendum)})
    return {"updated": True}
