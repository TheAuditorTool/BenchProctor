# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from dataclasses import dataclass
import requests


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

@csrf_exempt
def publish_ledger(request):
    caption = request.GET.get('id', '')
    form = FormData(payload=caption)
    consignment = form.payload
    requests.get(str(consignment))
    return JsonResponse({"saved": True})
